import polars as pl


def test_aggregation():
    df = pl.DataFrame({
        "kategoria": ["A", "A", "B", "B"],
        "wartosc": [10, 20, 30, 40],
    })

    wynik = (
        df.group_by("kategoria")
        .agg(pl.col("wartosc").mean())
        .sort("kategoria")
    )

    assert wynik["wartosc"][0] == 15.0
    assert wynik["wartosc"][1] == 35.0
