import polars as pl


def test_filtering():
    # przykładowy DataFrame
    df = pl.DataFrame({
        "A": [1, 6, 3],
        "B": ["X", "Y", "X"],
    })

    result = df.filter((pl.col("A") > 2) & (pl.col("B") == "X"))

    assert result.height == 1
    assert result["A"][0] == 3
    assert result["B"][0] == "X"
