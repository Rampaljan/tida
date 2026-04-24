import polars as pl


def test_dataframe_creation():
    # tworzymy ramkę danych z listy słowników
    data = [
        {"a": 1, "b": "x"},
        {"a": 2, "b": "y"},
    ]
    df = pl.DataFrame(data)

    # sprawdzamy kształt i kolumny
    assert df.shape == (2, 2)
    assert list(df.columns) == ["a", "b"]
