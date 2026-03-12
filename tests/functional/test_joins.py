import polars as pl


def test_joins():
    left = pl.DataFrame({
        "key": [1, 2, 3],
        "val": [10, 20, 30],
    })
    right = pl.DataFrame({
        "key": [2, 3, 4],
        "val2": [200, 300, 400],
    })

    joined = left.join(right, on="key", how="inner")

    assert joined.height == 2
    assert list(joined["val"]) == [20, 30]
    assert list(joined["val2"]) == [200, 300]
