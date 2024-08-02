import polars as pl

TARGET_COLUMNS = [
    "timestamp",
    "project_name",
    "version",
    "major_version",
    "type",
    "installer",
    "python",
    "major_python",
    "implementation",
    "distro",
    "system",
    "cpu",
]


def unnest_data(
    df: pl.DataFrame, target_columns: list[str] = TARGET_COLUMNS
) -> pl.DataFrame:
    df = (
        df.rename({"project": "project_name"})
        .unnest("file", "details")
        .with_columns(
            pl.col(["version", "python"])
            .str.split(".")
            .list.slice(0, 2)
            .list.join(".")
            .name.prefix("major_")
        )
        .select(target_columns)
    )
    return df
