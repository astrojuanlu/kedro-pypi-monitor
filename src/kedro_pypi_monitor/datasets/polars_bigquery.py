import contextlib
import logging
import os
import typing as t

import polars as pl
from google.cloud import bigquery
from kedro.io import AbstractDataset

logger = logging.getLogger()


@contextlib.contextmanager
def _set_env(**environ):
    """
    Temporarily set the process environment variables.

    >>> with set_env(PLUGINS_DIR='test/plugins'):
    ...   "PLUGINS_DIR" in os.environ
    True

    >>> "PLUGINS_DIR" in os.environ
    False

    :type environ: dict[str, unicode]
    :param environ: Environment variables to set
    """
    # https://stackoverflow.com/a/34333710
    old_environ = dict(os.environ)
    os.environ.update(environ)
    try:
        yield
    finally:
        os.environ.clear()
        os.environ.update(old_environ)


class PolarsBigQueryDataset(AbstractDataset):
    def __init__(self, sql: str, credentials: dict[str, t.Any] | None = None):
        self._sql = sql

        self._client = bigquery.Client.from_service_account_info(credentials)

    def _load(self):
        query_job = self._client.query(self._sql)

        # https://github.com/danielmiessler/fabric/discussions/754#discussioncomment-10120044
        with _set_env(GRPC_VERBOSITY="NONE"):
            df = pl.from_arrow(query_job.to_arrow())

        # https://github.com/ofek/pypinfo/blob/0720138/pypinfo/cli.py#L178-L184
        bytes_billed = query_job.total_bytes_billed or 0
        billing_tier = query_job.billing_tier or 1
        logger.debug("Bytes billed: %d, billing tier %d", bytes_billed, billing_tier)

        return df

    def _save(self, data: t.Any) -> None:
        raise NotImplementedError("Saving data not supported yet")

    def _describe(self) -> dict[str, t.Any]:
        return {"sql": self._sql}
