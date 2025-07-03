# BigData - Kurs Praktyczny

Ten projekt ilustruje praktyczne aspekty pracy z Big Data, od analizy wydajności narzędzi przez modelowanie predykcyjne po wdrożenie produkcyjne. Prezentuje kompletny pipeline danych w kontekście biznesowym.

## 📁 Struktura

### 1. **Dane** - Analiza wydajności narzędzi przetwarzania danych
**Cel:** Demonstracja ograniczeń tradycyjnych narzędzi i przewag nowoczesnych baz analitycznych

**Zawartość:**
- Porównanie wydajności **Pandas vs DuckDB** na różnych wolumenach danych (100K, 10M, 100M rekordów)
- Praktyczne pokazanie problemów z pamięcią przy dużych zbiorach danych
- Monitoring zasobów systemowych podczas przetwarzania
- Wizualizacja różnic wydajności

**Technologie:** pandas, DuckDB, psutil, matplotlib, seaborn

### 2. **Modele** - Automatyczne uczenie maszynowe
**Cel:** Budowa modeli predykcyjnych dla szeregów czasowych

**Zawartość:**
- Trenowanie modelu predykcji sprzedaży alkoholi w Iowa
- Wykorzystanie **AutoGluon** do automatycznego dostrajania modeli
- Predykcja popytu na 7 dni dla różnych produktów
- Eksploracja danych czasowych z wieloma elementami

**Technologie:** AutoGluon, pandas, matplotlib

### 3. **Uruchomienie** - Wdrożenie aplikacji predykcyjnej
**Cel:** Demonstracja różnych strategii deployment od lokalnego po chmurowe

#### 3.1 **Local** - Uruchomienie lokalne
- Serwer **FastAPI** z endpointem predykcyjnym
- Aplikacja **Streamlit** z interfejsem użytkownika
- Testowanie API na lokalnym środowisku

#### 3.2 **Docker** - Konteneryzacja
- Dockeryzacja aplikacji z użyciem **uv** jako menedżera pakietów
- Budowa i uruchomienie kontenerów
- Izolacja środowiska i reproducibility

#### 3.3 **GCP Run** - Wdrożenie w chmurze
- Deployment na **Google Cloud Run**
- Konfiguracja registry i tagowanie obrazów
- Skalowanie automatyczne w środowisku chmurowym

**Technologie:** FastAPI, Streamlit, Docker, Google Cloud Run

### 4. **Wydajność** - Testowanie obciążenia
**Cel:** Ocena wydajności aplikacji pod obciążeniem

**Zawartość:**
- Testy obciążeniowe z użyciem **Locust**
- Symulacja 1000 użytkowników równocześnie
- Testowanie zarówno lokalnie jak i w chmurze
- Analiza metryk wydajności

**Technologie:** Locust, HTTP load testing

### 5. **Eksperymenty** - A/B testing i zarządzanie wersjami
**Cel:** Strategie wdrażania i testowania w produkcji

**Zawartość:**
- Chatbot z wykorzystaniem **OpenAI API**
- A/B testing przez traffic splitting (80/20)
- Deployment różnych wersji aplikacji
- Zarządzanie ruchem między wersjami

**Technologie:** OpenAI API, Streamlit, traffic management

## 🎯 Cele dydaktyczne

### Obszary BigData omawiane w kursie:
1. **Wydajność przetwarzania** - wpływ wyboru technologii na skalowalność
2. **Machine Learning** - automatyzacja procesu budowy modeli
3. **Deployment strategies** - od lokalnego do chmurowego
4. **Performance testing** - testowanie systemów pod obciążeniem
5. **Experimentation** - A/B testing i canary deployment

### Kluczowe umiejętności:
- Optymalizacja zapytań i zarządzanie pamięcią
- Automatyczne uczenie maszynowe (AutoML)
- Konteneryzacja i wdrażanie aplikacji
- Testowanie wydajności i obciążenia
- Strategie eksperymentowania w produkcji

## 🚀 Technologie

**Przetwarzanie danych:** pandas, DuckDB  
**Machine Learning:** AutoGluon  
**Backend:** FastAPI, uvicorn  
**Frontend:** Streamlit  
**Deployment:** Docker, Google Cloud Run  
**Testing:** Locust  
**AI Integration:** OpenAI API  

## 📊 Praktyczne zastosowania

Projekt koncentruje się na rzeczywistych scenariuszach biznesowych:
- Analiza sprzedaży detalicznej (dane z Iowa)
- Optymalizacja kosztów infrastruktury
- Skalowanie aplikacji ML w chmurze
- Monitoring wydajności systemów produkcyjnych

Każdy folder zawiera praktyczne przykłady z instrukcjami krok po kroku, umożliwiającymi samodzielne odtworzenie i eksperymentowanie z przedstawionymi rozwiązaniami.