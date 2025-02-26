# QR Kod Generator

Detta projekt är en enkel Flask-baserad webapplikation som genererar QR-koder från angivna URL:er. QR-koderna lagras och visas på sidan.

## Funktioner
- Genererar QR-koder baserat på användarinmatad URL.
- Visar tidigare genererade QR-koder på sidan.
- Enkel och responsiv design med mörkgrön färg.

## Installation och körning
### 1. Klona eller ladda ner projektet
```bash
git clone <repo-url>
cd <projektmapp>
```

### 2. Installera beroenden
```bash
pip install flask qrcode[pil]
```

### 3. Starta Flask-applikationen
```bash
python qr-kod.py
```

### 4. Öppna i webbläsaren
Gå till:
```
http://127.0.0.1:5000/
```

## Filstruktur
```
/project-root
│── qr-kod.py  # Flask-backend
│── templates/
│   ├── index.html  # Webbgränssnitt
```

## Teknologier
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **QR-kodgenerering**: qrcode-biblioteket

## Förbättringar
- Möjlighet att ladda ner QR-koder.
- Lokal databaslagring av QR-koder.
- Möjlighet att anpassa storlek och färg på QR-koder.

---
**Skapad av Sivert Kandlan 2023/12/05**

