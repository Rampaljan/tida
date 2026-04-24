import polars as pl
import time


def test_perf_filter_large_dataframe():
    """Pomiar czasu filtrowania miliona wierszy."""
    start = time.perf_counter()
    df_large = pl.DataFrame({
        "id": range(1_000_000),
        "dane": range(1_000_000),
    })
    _ = df_large.filter(pl.col("id") > 500_000)
    duration = time.perf_counter() - start
    print(f"[PERF] filtrowanie 1 mln wierszy trwa {duration:.4f}s")

    # podstawowe kryterium wydajności
    assert duration < 0.5
