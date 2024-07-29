"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.6
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import unnest_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=unnest_data,
                inputs="pypi_kedro_raw",
                outputs="pypi_kedro",
            )
        ]
    )
