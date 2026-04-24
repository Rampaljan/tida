# Dokumentacja Scenariuszy Testów Akceptacyjnych (UAT)
**Moduł:** Polars (PyPI)
**Zespół:** Adam, Janek, Natalia

## Wstęp
Niniejszy dokument opisuje scenariusze akceptacyjne dla systemu testowania OOB modułu Polars. Scenariusze te służą do końcowej weryfikacji, czy biblioteka spełnia podstawowe wymagania użytkowe i wydajnościowe[cite: 3, 50].

---

### Scenariusz 1: Poprawność instalacji i importu "Out Of The Box"
* **Cel testu:** Weryfikacja, czy najnowsza stabilna wersja Polars z repozytorium PyPI instaluje się bezbłędnie w standardowym środowisku Python[cite: 29].
* **Opis oczekiwanego rezultatu:** Proces instalacji kończy się sukcesem, a wykonanie polecenia `import polars` w konsoli nie generuje żadnych błędów[cite: 53].
* **Kryterium zaliczenia:** Brak komunikatów o błędach (Errors) podczas instalacji oraz pomyślne zaczytanie biblioteki przez interpreter[cite: 54].

---

### Scenariusz 2: Integralność filtrowania i agregacji danych
* **Cel testu:** Sprawdzenie, czy podstawowe funkcje manipulacji danymi (filtrowanie i grupowanie) zwracają poprawne wyniki logiczne na zbiorze testowym[cite: 39].
* **Opis oczekiwanego rezultatu:** Po nałożeniu filtra na kolumnę numeryczną i wykonaniu operacji `mean()`, otrzymany wynik jest zgodny z ręcznie wyliczoną wartością wzorcową[cite: 53].
* **Kryterium zaliczenia:** Wartości w wynikowej ramce danych (DataFrame) są identyczne z założonymi w scenariuszu testowym (Test PASS)[cite: 54].

---

### Scenariusz 3: Wydajność przetwarzania dużych wolumenów danych
* **Cel testu:** Pomiar czasu wykonania operacji sortowania oraz zapisu dla ramki danych zawierającej 1 000 000 rekordów[cite: 32, 46].
* **Opis oczekiwanego rezultatu:** Operacja zostaje wykonana, a zmierzony czas trwania zostaje odnotowany w logach systemu[cite: 47, 53].
* **Kryterium zaliczenia:** Całkowity czas operacji nie przekracza 2 sekund (wartość przyjęta dla standardowego środowiska GitHub Actions), a wynik pomiaru jest widoczny w raporcie końcowym[cite: 48, 54].

---

### Scenariusz 4 (Opcjonalny): Stabilność typowania kolumn
* **Cel testu:** Weryfikacja, czy Polars poprawnie rozpoznaje typy danych (Schema) podczas wczytywania plików CSV[cite: 152].
* **Opis oczekiwanego rezultatu:** Kolumny zawierające liczby są rozpoznawane jako typy Int/Float, a kolumny tekstowe jako String[cite: 53].
* **Kryterium zaliczenia:** Metoda `df.schema` zwraca typy zgodne ze strukturą pliku wejściowego[cite: 54].
