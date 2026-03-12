# Projekt OOB: Testowanie modułu Polars

## 📋 Spis treści
- [Opis projektu](#opis-projektu)
- [Cel projektu](#cel-projektu)
- [Zespół i role](#zespół-i-role)
- [Harmonogram](#harmonogram)
- [Komunikacja](#komunikacja)
- [Dlaczego Polars?](#dlaczego-polars)
- [Strategia testowa](#strategia-testowa)
- [Struktura repozytorium](#struktura-repozytorium)
- [Scenariusze testów akceptacyjnych](#scenariusze-testów-akceptacyjnych)
- [Plan testów funkcjonalnych](#plan-testów-funkcjonalnych)
- [Plan testów wydajnościowych](#plan-testów-wydajnościowych)
- [Pipeline CI/CD (GitHub Actions)](#pipeline-cicd-github-actions)
- [Instrukcja uruchomienia](#instrukcja-uruchomienia)
- [Podsumowanie](#podsumowanie)

---

## Opis projektu
Projekt realizowany w ramach przedmiotu „Projekt zespołowy” na Politechnice. Celem jest zaprojektowanie i wdrożenie uproszczonego systemu testowania **Out Of The Box (OOB)** dla biblioteki **Polars** dostępnej w repozytorium PyPI. System opiera się na ręcznie uruchamianej pipeline w GitHub Actions, która wykonuje testy funkcjonalne i wydajnościowe, a następnie prezentuje czytelne raporty.

---

## Cel projektu
- Praktyczne zapoznanie się z pracą zespołową na GitHubie (issues, pull requests, code review).
- Zrozumienie podstaw CI/CD poprzez implementację prostej pipeline w GitHub Actions.
- Projektowanie i wykonywanie testów funkcjonalnych oraz wydajnościowych.
- Opracowanie scenariuszy testów akceptacyjnych i dokumentacji projektowej.
- Organizacja pracy w zespole z podziałem ról i odpowiedzialności.

---

## Zespół i role
| Imię i nazwisko | Rola              | Odpowiedzialności |
|-----------------|-------------------|-------------------|
| **Natalia**     | DevOps Lead       | Konfiguracja CI/CD (GitHub Actions), automatyzacja instalacji i uruchamiania testów, struktura repozytorium |
| **Janek**       | QA Engineer       | Opracowanie i implementacja testów funkcjonalnych oraz wydajnościowych, analiza wyników |
| **Adam**        | Project Manager   | Dokumentacja, harmonogram, scenariusze akceptacyjne, spójność projektu, koordynacja prac |

---

## Harmonogram
| Etap                   | Termin          | Zadania |
|------------------------|-----------------|---------|
| **Punkt kontrolny 1**  | Marzec 2026     | Organizacja, założenie repozytorium, README, harmonogram, role, wstępne scenariusze testów |
| **Punkt kontrolny 2**  | Kwiecień 2026   | Zarządzanie kodem, Pull Requesty, Issues, code review |
| **Punkt kontrolny 3**  | Maj 2026        | Pełna implementacja testów, działająca pipeline, raportowanie |
| **Final Release**      | Koniec maja 2026 | Prezentacja projektu, kompletna dokumentacja, samoocena zespołu |

---

## Komunikacja
- **Bieżące ustalenia:** Kanał na Discordzie
- **Zarządzanie zadaniami:** GitHub Issues
- **Tablica projektu:** GitHub Projects (wizualizacja postępu)
- **Spotkania tygodniowe:** Synchronizacja postępów (ustalony termin)

---

## Dlaczego Polars?
Do testowania wybraliśmy moduł **Polars** – nowoczesną bibliotekę DataFrame napisaną w Rusta, oferującą wysoką wydajność i wygodne API. Główne powody wyboru:
- **Popularność i rosnące znaczenie** – Polars zyskuje uznanie jako szybsza alternatywa dla pandas.
- **Bogactwo funkcji** – obsługa grupowań, łączeń, agregacji, przetwarzania strumieniowego – szerokie pole do testowania.
- **Wyraźne różnice w wydajności** – łatwo zaprojektować testy porównawcze.
- **Dokumentacja i stabilne API** – ułatwia pisanie testów.

Testujemy **najnowszą stabilną wersję** z PyPI (zgodnie z zakresem podstawowym).

---

## Strategia testowa
Testowanie modułu Polars będzie realizowane na trzech poziomach:
1. **Testy funkcjonalne** – autorskie scenariusze sprawdzające poprawność działania kluczowych mechanizmów.
2. **Testy wydajnościowe** – proste pomiary czasu wykonywania wybranych operacji z zapisem wyników do logu.
3. **Testy akceptacyjne** – scenariusze opisowe, weryfikowane ręcznie (nieautomatyzowane).

Wszystkie testy zostaną zautomatyzowane w pipeline GitHub Actions. Wyniki będą prezentowane w czytelnej formie (podsumowanie w konsoli, pliki z logami jako artefakty).

---

## Struktura repozytorium
```
.
├── .github/
│   └── workflows/
│       └── main.yml                # Definicja pipeline GitHub Actions
├── docs/
│   ├── acceptance_scenarios.md     # Scenariusze testów akceptacyjnych
│   └── reports/                     # Miejsce na raporty (logi, wyniki)
├── tests/
│   ├── functional/
│   │   ├── test_dataframe_creation.py
│   │   ├── test_filtering.py
│   │   ├── test_joins.py
│   │   └── ...
│   ├── performance/
│   │   ├── test_csv_load_perf.py
│   │   └── log_perf.txt             # Wyniki testów wydajnościowych
│   └── conftest.py                  # Konfiguracja pytest (jeśli potrzebna)
├── requirements.txt                  # Zależności do uruchomienia testów
├── README.md                         # Niniejszy plik
└── .gitignore
```

---

## Scenariusze testów akceptacyjnych
Dokument z co najmniej 3 scenariuszami znajduje się w pliku:  
📄 [`docs/acceptance_scenarios.md`](docs/acceptance_scenarios.md)

### Streszczenie scenariuszy:
| Scenariusz | Cel | Oczekiwany rezultat | Kryterium zaliczenia |
|------------|-----|---------------------|----------------------|
| **Instalacja OOB** | Sprawdzenie, czy biblioteka instaluje się bez błędów w czystym środowisku | `pip install polars` kończy się sukcesem | Brak błędów w logach instalacji |
| **Agregacja danych** | Weryfikacja poprawności obliczeń statystycznych | Średnia z kolumny numerycznej zgodna z danymi testowymi | Wynik zgodny z oczekiwaniami |
| **Wsparcie formatów** | Odczyt pliku CSV o rozmiarze >100MB | Czas odczytu mieści się w założonym limicie | Pomiar czasu < założony próg |

---

## Plan testów funkcjonalnych
Janek (QA) przygotuje **4 testy funkcjonalne** (zakres 3–5). Każdy test sprawdza realne użycie modułu.

| Nazwa testu | Opis | Uzasadnienie |
|-------------|------|--------------|
| **Tworzenie DataFrame** | Utworzenie DataFrame z listy słowników i weryfikacja schematu (kolumny, typy) | Podstawowa operacja – musi działać niezawodnie |
| **Złożone filtrowanie** | Filtrowanie z użyciem wielu warunków: `df.filter((pl.col("A") > 5) & (pl.col("B") == "X"))` | Częste w analizie danych – testuje poprawność wyrażeń logicznych |
| **Operacja join** | Połączenie dwóch DataFrame na wspólnej kolumnie i sprawdzenie liczby wierszy | Kluczowa funkcjonalność przy łączeniu danych |
| **Agregacje grupowe** | Grupowanie danych i obliczanie sum, średnich, wartości minimalnych/maksymalnych | Sprawdza poprawność operacji grupujących |

Testy zostaną napisane z użyciem frameworka `pytest` i będą porównywać wyniki z wartościami oczekiwanymi.

---

## Plan testów wydajnościowych
Przygotujemy **1–2 proste testy wydajnościowe** mierzące czas wykonania wybranych operacji.

| Nazwa testu | Opis | Sposób pomiaru |
|-------------|------|----------------|
| **Wczytywanie dużego CSV** | Pomiar czasu wczytywania pliku CSV o rozmiarze >100 MB | `time.perf_counter()` – wynik zapisany do pliku `tests/performance/log_perf.txt` |

Wyniki będą przechowywane jako artefakty w pipeline, co pozwoli na prostą analizę porównawczą.

---

## Pipeline CI/CD (GitHub Actions)
Pipeline jest zdefiniowana w pliku `.github/workflows/main.yml` i uruchamiana **ręcznie** (`workflow_dispatch`).

### Kroki pipeline:
1. **Ustawienie środowiska** (ubuntu-latest, Python 3.10)
2. **Instalacja Polars** z PyPI
3. **Uruchomienie testów funkcjonalnych** (wszystkie pliki `tests/functional/test_*.py`)
4. **Uruchomienie testów wydajnościowych** (np. `tests/performance/test_csv_load_perf.py`)
5. **Prezentacja podsumowania** – logi z wynikami, artefakty z plikami pomiarów

### Szkic pipeline:
```yaml
name: OOB Polars Testing
on:
  workflow_dispatch:  # Uruchamianie manualne

jobs:
  test-polars:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install Polars
        run: pip install polars
      - name: Install test dependencies
        run: pip install pytest
      - name: Run Functional Tests
        run: pytest tests/functional/ --verbose
      - name: Run Performance Tests
        run: pytest tests/performance/ --verbose --log-cli-level=INFO
      - name: Upload performance logs
        uses: actions/upload-artifact@v4
        with:
          name: performance-logs
          path: tests/performance/log_perf.txt
```

---

## Instrukcja uruchomienia
### Lokalnie
1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/Rampaljan/tida
   cd polars-testing
   ```
2. (Opcjonalnie) Utwórz i aktywuj wirtualne środowisko.
3. Zainstaluj zależności:
   ```bash
   pip install -r requirements.txt
   ```
4. Zainstaluj Polars:
   ```bash
   pip install polars
   ```
5. Uruchom testy funkcjonalne:
   ```bash
   pytest tests/functional/
   ```
6. Uruchom testy wydajnościowe:
   ```bash
   pytest tests/performance/ --log-cli-level=INFO
   ```

### Na GitHubie
1. Przejdź do zakładki **Actions** w repozytorium.
2. Wybierz workflow **OOB Polars Testing**.
3. Kliknij **Run workflow** (wybierz gałąź `main`).
4. Po zakończeniu sprawdź logi i pobierz artefakty z wynikami.

---

## Podsumowanie
Projekt ma na celu nie tylko techniczne sprawdzenie modułu Polars, ale przede wszystkim naukę organizacji pracy zespołowej, korzystania z nowoczesnych narzędzi CI/CD oraz tworzenia wartościowych testów. Dzięki podziałowi ról (DevOps, QA, PM) każdy członek zespołu zdobędzie praktyczne doświadczenie w swojej dziedzinie.

Wszelkie uwagi i pytania prosimy zgłaszać poprzez **Issues** w repozytorium.

---
📅 **Projekt realizowany**: marzec – maj 2026  
👥 **Zespół**: Natalia, Janek, Adam  
🔗 **Repozytorium**: [github.com/twoja-organizacja/polars-testing](https://github.com/twoja-organizacja/polars-testing)