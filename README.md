Projekt OOB: Testowanie modułu Polars 

Zespół: Natalia (DevOps), Janek (QA), Adam (PM). 

Cel projektu 

Celem jest zaprojektowanie systemu testowania Out Of The Box dla biblioteki Polars dostępnej w PyPI. Skupiamy się na weryfikacji funkcjonalnej i wydajnościowej najnowszej stabilnej wersji. 

### Podział ról  

Natalia (DevOps Lead): Konfiguracja CI/CD (GitHub Actions), automatyzacja instalacji i uruchamiania testów. 

Janek (QA Engineer): Opracowanie i implementacja testów funkcjonalnych oraz wydajnościowych. 

Adam (Project Manager): Dokumentacja, harmonogram, scenariusze akceptacyjne i spójność projektu. 

### Harmonogram * Punkt Kontrolny 1 (Marzec 2026): Organizacja, repozytorium i planowanie. * Punkt Kontrolny 2 (Kwiecień 2026): Zarządzanie kodem, Pull Requesty i Issues. * Punkt Kontrolny 3 (Maj 2026): Pełna implementacja testów i działająca pipeline. * Final Release (Koniec Maja 2026): Prezentacja i raport końcowy. 

### Komunikacja  

Bieżące ustalenia: Kanał na Discordzie. 

Zarządzanie zadaniami: GitHub Issues. 

2. Plik docs/acceptance_scenarios.md  

Przygotuj dokument z co najmniej 3 scenariuszami: 

Scenariusz 1: Instalacja OOB 

Cel: Sprawdzenie, czy biblioteka instaluje się bez błędów w czystym środowisku. 

Oczekiwany rezultat: pip install polars kończy się sukcesem. 

Kryterium: Brak błędów w logach instalacji. 

Scenariusz 2: Agregacja danych 

Cel: Weryfikacja poprawności obliczeń statystycznych. 

Rezultat: Średnia z kolumny numerycznej jest zgodna z danymi testowymi. 

Scenariusz 3: Wsparcie formatów 

Cel: Odczyt pliku CSV o rozmiarze powyżej 100MB. 

Kryterium: Czas odczytu mieści się w założonym limicie (test wydajnościowy). 

 

Zadania dla Natalii (DevOps & Pipeline Lead) 

Twoim zadaniem jest przygotowanie struktury i mechanizmu automatyzacji. 

1. Struktura katalogów  

Stwórz w repozytorium następujące foldery: 

tests/functional/ – na testy Janka. 

tests/performance/ – na pomiary wydajności. 

docs/ – na dokumenty Adama. 

.github/workflows/ – na Twoją pipeline. 

2. Szkic Pipeline (.github/workflows/main.yml) 

Skonfiguruj manualnie uruchamiany proces: 

YAML 

name: OOB Polars Testing 
on: 
 [cite_start]workflow_dispatch: # Uruchamianie manualne  
 
jobs: 
 test-polars: 
   runs-on: ubuntu-latest 
   steps: 
     - uses: actions/checkout@v4 
     - name: Install Polars 
       [cite_start]run: pip install polars # Instalacja z PyPI [cite: 29] 
     - name: Run Functional Tests 
       [cite_start]run: echo "Tu Janek doda testy funkcjonalne" [cite: 31] 
     - name: Run Performance Tests 
       [cite_start]run: echo "Tu Janek doda testy wydajnościowe" [cite: 32] 
 

 

Zadania dla Janka (QA & Test Engineer) 

Twoim zadaniem jest zaplanowanie konkretnych testów, które wykonasz w kolejnych etapach. 

1. Plan Testów Funkcjonalnych (3-5 testów)  

Test 1: Tworzenie DataFrame z listy słowników i weryfikacja schematu. 

Test 2: Złożone filtrowanie (np. df.filter((pl.col("A") > 5) & (pl.col("B") == "X"))). 

Test 3: Operacja join na dwóch ramkach danych i sprawdzenie liczby wierszy wyniku. 

2. Plan Testów Wydajnościowych (1-2 testy)  

Test 1: Pomiar czasu wczytywania dużego pliku CSV (wykorzystaj moduł time). 

Zadanie dodatkowe: Zapisz wynik (czas w sekundach) do pliku tekstowego log_perf.txt, aby Natalia mogła go wyświetlić w podsumowaniu pipeline. 

 
