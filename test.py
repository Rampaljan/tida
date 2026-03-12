import polars as pl
import time
import pytest

# 1. TEST FUNKCJONALNY - Sprawdzenie agregacji [cite: 37, 39]
def test_polars_aggregation():
    df = pl.DataFrame({
        "kategoria": ["A", "A", "B", "B"],
        "wartosc": [10, 20, 30, 40]
    })
    
    # Obliczamy średnią dla każdej kategorii
    wynik = df.group_by("kategoria").agg(pl.col("wartosc").mean()).sort("kategoria")
    
    assert wynik["wartosc"][0] == 15.0  # Średnia dla A
    assert wynik["wartosc"][1] == 35.0  # Średnia dla B

# 2. TEST WYDAJNOŚCIOWY - Pomiar czasu operacji [cite: 44, 46]
def test_polars_performance_simple():
    # Tworzymy dużą ramkę danych (1 milion wierszy)
    start_time = time.time()
    
    df_large = pl.DataFrame({
        "id": range(1_000_000),
        "dane": range(1_000_000)
    })
    
    # Wykonujemy operację filtrowania
    _ = df_large.filter(pl.col("id") > 500_000)
    
    end_time = time.time()
    duration = end_time - start_time
    
    # Zapis wyniku do loga [cite: 47]
    print(f"\n[PERF] Czas filtrowania 1 mln wierszy: {duration:.4f} s")
    
    # Proste porównanie - test przechodzi, jeśli trwa poniżej 0.5s [cite: 48, 54]
    assert duration < 0.5