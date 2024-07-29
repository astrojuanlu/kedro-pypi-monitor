"""
This is a boilerplate pipeline 'fetch_demo'
generated using Kedro 0.19.6
"""

from kedro.pipeline import Pipeline, node, pipeline

from ..data_processing.nodes import unnest_data
from .nodes import exclude_nested_dtypes


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=unnest_data,
                inputs="pypi_kedro_raw",
                outputs="pypi_kedro_unnested",
            ),
            node(
                func=exclude_nested_dtypes,
                inputs="pypi_kedro_unnested",
                outputs="pypi_kedro_demo",
            ),
        ]
    )
