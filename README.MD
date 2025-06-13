# AI Test Assistant

**AI Test Assistant** to aplikacja webowa wykorzystująca Google Gemini do automatycznego generowania testów jednostkowych, analizy bezpieczeństwa kodu oraz weryfikacji zasad SOLID.

## Funkcje

- Generowanie testów jednostkowych na podstawie kodu źródłowego
- Analiza bezpieczeństwa kodu
- Sprawdzenie zgodności kodu z zasadami SOLID:
  - SRP (Single Responsibility Principle)
  - OCP (Open/Closed Principle)
  - LSP (Liskov Substitution Principle)
  - ISP (Interface Segregation Principle)
  - DIP (Dependency Inversion Principle)
- Obsługa plików `.py`, `.js`, `.ts`, `.html`, `.php`, `.txt`, `.java`
- Możliwość wklejania kodu lub przesyłania plików
- Tryb ciemny i jasny z zapamiętywaniem preferencji

## Wymagania

- Python 3.8+
- Klucz API do Google Gemini (`GEMINI_API_KEY` w pliku `.env`)
- Flask
- Biblioteka `google-generativeai`

## Struktura projektu

- `app.py` – główny plik backendu z wykorzystaniem Flask i Google Gemini
- `prompts.py` – zestaw predefiniowanych promptów (QA, bezpieczeństwo, SOLID)
- `.env` – plik konfiguracyjny z kluczem API do Gemini (`GEMINI_API_KEY`)
- `templates/`
  - `index.html` – szablon HTML dla głównego interfejsu
- `static/`
  - `style.css` – arkusz stylów (motyw jasny i ciemny)
  - `script.js` – plik JavaScript obsługujący UI i integrację z backendem
- `README.md` – dokumentacja projektu
- `requirements.txt` - lista wymaganych bibliotek Pythona