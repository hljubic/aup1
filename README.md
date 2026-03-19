# Flask projekt – osnovno postavljanje

Ovaj projekt prikazuje osnovno korištenje Flask frameworka u Pythonu, uključujući rad s virtualnim okruženjem (`venv`) i upravljanje paketima putem `pip`.

---

## Virtual environment (ručno postavljanje)

Ako ne koristiš PyCharm ili drugi IDE za automatsko upravljanje okruženjem, možeš sve postaviti ručno.

### 1. Kreiranje virtualnog okruženja

```bash
python -m venv venv
```

### 2. Aktivacija virtualnog okruženja

**macOS / Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

---

## PIP i instalacija paketa

### 3. Provjera PIP-a

```bash
python -m pip --version
```

Ako dobiješ grešku `ModuleNotFoundError`, pokreni:

```bash
python -m ensurepip --upgrade
```

---

### 4. Instalacija Flaska

```bash
python -m pip install flask
```

---

### 5. Spremanje instaliranih paketa

Kad instaliraš nove biblioteke:

```bash
python -m pip freeze > requirements.txt
```

---

### 6. Instalacija svih paketa iz requirements.txt

```bash
python -m pip install -r requirements.txt
```

---

## Pokretanje aplikacije

```bash
python main.py
```

---

## 📁 Preporučena struktura projekta

```
projekt/
│── venv/
│── main.py
│── requirements.txt
│── templates/
│── static/
```

---

## Napomene

* Virtualno okruženje (`venv`) se **ne commita na Git**
* `requirements.txt` služi za dijeljenje ovisnosti
* Preporučuje se uvijek koristiti:

```bash
python -m pip ...
```

umjesto samo `pip`, kako bi bio siguran da koristiš ispravan interpreter

---

## 📄 .gitignore

Dodaj `.gitignore` datoteku u root projekta:

```gitignore
# Virtual environment
venv/

# Environment variables
.env
.env.*

# IDE
.vscode/
.idea/
```

---

## Brzi start

```bash
python -m venv venv
venv\Scripts\activate # Windows verzija
source venv/bin/activate   # Linux verzija
python -m pip install flask
python main.py
```

---
