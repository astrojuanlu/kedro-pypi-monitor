"""
This is a boilerplate pipeline 'fetch_demo'
generated using Kedro 0.19.6
"""

import ibis
import polars as pl
import polars.selectors as cs


def filter_data(
    table: ibis.Table, start_time: str = "2024-07-01", end_time: str = "2024-07-02"
) -> ibis.Table:
    table = table.filter(
        [
            table.project == "kedro",
            ibis.timestamp(start_time) <= table.timestamp,
            table.timestamp < ibis.timestamp(end_time),
        ]
    )
    return table


def exclude_nested_dtypes(df: pl.DataFrame) -> pl.DataFrame:
    return df.select(cs.datetime(), cs.string())
