"""
This is a boilerplate pipeline 'fetch_demo'
generated using Kedro 0.19.6
"""

import polars as pl
import polars.selectors as cs


def exclude_nested_dtypes(df: pl.DataFrame) -> pl.DataFrame:
    return df.select(cs.datetime(), cs.string())
