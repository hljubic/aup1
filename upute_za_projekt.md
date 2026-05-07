# Upute za projekt

Ovaj projekt služi kao **template** za studentski rad. Studenti ga mogu uzeti kao osnovu, ali trebaju napraviti vlastitu temu, vlastite tablice i vlastiti flow aplikacije.

Template već pokazuje:

- Flask backend
- Vue + Vuetify frontend
- CRUD operacije
- relacije između tablica
- pregled pojedinačnog zapisa
- pretragu
- paginaciju
- dropdown za strane ključeve

## 1. Što student mora napraviti

Svaki student treba napraviti vlastiti projekt na nekoj smislenoj temi.

Primjeri tema:

- knjižnica
- videoteka
- restoran
- škola
- ordinacija
- webshop
- turistička agencija
- teretana

Tema je slobodna, ali projekt mora imati smisla i mora koristiti bazu podataka.

## 2. Minimalni projektni zahtjevi

Projekt mora imati:

- najmanje **4 tablice** u bazi podataka
- relacije između tablica gdje to ima smisla
- backend napravljen u Flasku
- frontend napravljen u Vue + Vuetify
- CRUD operacije za najmanje 4 tablice
- početnu stranicu kao jednostavan dashboard

Projekt mora biti organiziran u **dva odvojena GitHub repozitorija**:

- jedan repozitorij za backend
- jedan repozitorij za frontend

CRUD znači:

- `Create` = dodavanje novog zapisa
- `Read` = ispis zapisa
- `Update` = uređivanje zapisa
- `Delete` = brisanje zapisa

## 3. Primjeri tablica

Primjer za školu:

- `profesori`
- `kolegiji`
- `ucionice`
- `termini_nastave`

Primjer za knjižnicu:

- `knjige`
- `autori`
- `clanovi`
- `posudbe`

Primjer za webshop:

- `proizvodi`
- `kategorije`
- `kupci`
- `narudzbe`

Bitno je da tablice nisu nasumične, nego da čine jednu cjelinu.

## 4. Predaja projekta

Prije ispitnog roka studenti moraju poslati projekt na mail:

```text
hrvoje.ljubic@fpmoz.sum.ba
```

U mailu trebaju poslati:

- link na GitHub repozitorij za backend
- link na GitHub repozitorij za frontend

Frontend i backend trebaju biti u **dva odvojena repozitorija**.

## 5. Dashboard na početnoj stranici

Početna stranica ne bi trebala biti prazna. Trebala bi služiti kao jednostavan **Dashboard**.

Na dashboardu student treba prikazati nekoliko osnovnih informacija iz baze podataka, na primjer:

- ukupan broj profesora
- ukupan broj kolegija
- ukupan broj učionica
- prosječan broj ECTS bodova
- broj aktivnih narudžbi, posudbi, termina ili slično, ovisno o temi projekta

Ne mora biti ništa komplicirano. Cilj je pokazati da student zna dohvatiti podatke iz baze i prikazati ih na početnoj stranici.

## 6. Što već postoji u templateu

Backend primjer pokazuje:

- liste zapisa
- dohvat jednog zapisa po ID-u
- dodavanje
- uređivanje
- brisanje
- relaciju `kolegij -> profesor`
- dropdown podatke preko API-ja
- backend pretragu
- backend paginaciju

Frontend primjer pokazuje:

- tablični pregled
- gumb `Dodaj`
- forma za dodavanje
- forma za uređivanje s prepopunjenim podacima
- akcije u tablici
- potvrdu brisanja kroz dialog
- pregled pojedinačnog zapisa
- search input
- prikaz paginacije
- padajući izbornik za povezane podatke

## 7. Ocjena 2

Za ocjenu **2** student mora znati najtemeljnije stvari i mora moći podići projekt od nule.

Očekuje se razumijevanje:

- `v-model`
- `v-if`
- `@click` i drugi osnovni `@event` događaji
- `ref`
- `reactive`
- razlika između `const` i `let`
- osnovni `fetch`
- što je ruta
- što je model
- što je migracija
- što radi `flask db init`
- što radi `flask db migrate`
- što radi `flask db upgrade`
- što je virtualno okruženje
- čemu služi `node_modules`

Za ocjenu 2 student mora moći objasniti osnovni tok aplikacije:

1. napravi se baza
2. pokrenu se migracije
3. pokrene se backend
4. pokrene se frontend
5. frontend zove backend API

Za ocjenu 2 student treba imati i početnu dashboard stranicu s nekoliko osnovnih informacija iz baze.

## 8. Ispitni zadatak za ocjenu 2

Na ispitu se može tražiti da student pobriše generirane foldere i ponovno podigne projekt od početka.

Generirani folderi u ovom projektu su tipično:

- `.venv`
- `__pycache__`
- `aup-frontend/node_modules`
- `aup-frontend/dist`
- `aup-frontend/node_modules/.vite`
- `aup-frontend/node_modules/.vite-temp`

Student ne smije brisati važne konfiguracijske datoteke kao što su:

- `requirements.txt`
- `package.json`
- `package-lock.json`
- `pyproject.toml`

Student mora znati:

1. ponovno napraviti bazu podataka
2. ponovno napraviti ili aktivirati virtualno okruženje
3. ponovno instalirati backend pakete
4. ponovno instalirati frontend pakete
5. ponovno pokrenuti migracije
6. ponovno pokrenuti backend
7. ponovno pokrenuti frontend

Drugim riječima, student mora moći podići projekt **od nule**.

## 9. Ocjena 3

Za ocjenu **3** student mora napraviti osnovni funkcionalni projekt.

To znači:

- najmanje 4 tablice u bazi
- barem jedna relacija između tablica
- CRUD za najmanje 4 tablice
- backend rute rade ispravno
- frontend prikazuje podatke iz baze
- moguće je dodavanje, uređivanje i brisanje
- podaci se stvarno spremaju u bazu
- dashboard prikazuje osnovne podatke iz baze

Za ocjenu 3 projekt ne mora biti posebno napredan, ali mora biti **ispravan i funkcionalan**.

## 10. Ocjena 4

Za ocjenu **4** očekuje se uredniji i potpuniji projekt.

Uz sve iz ocjene 3, očekuje se još:

- više smislenih relacija između tablica
- pregled pojedinačnog zapisa
- potvrda prije brisanja
- **frontend pretraga**
- **frontend paginacija**
- dropdown za strane ključeve gdje to ima smisla
- uredniji frontend i bolji flow kroz stranice
- razumijevanje grid systema
- responsive prikaz na različitim veličinama ekrana
- bolji vizualni dojam od osnovnog templatea

Za ocjenu 4 student pokazuje da zna napraviti pregledan CRUD projekt. Pretraga i paginacija mogu biti napravljene na frontendu.

## 11. Ocjena 5

Za ocjenu **5** očekuje se ozbiljniji i dotjeraniji projekt.

Uz sve iz ocjene 4, očekuje se još:

- **backend pretraga**
- **backend paginacija**
- filteri gdje imaju smisla
- bolja validacija formi
- bolja obrada grešaka
- uredniji prikaz povezanih podataka
- dosljedan frontend
- bolji UX
- bolji vizualni dojam
- projekt kao zaokružena aplikacija, a ne samo skup CRUD primjera

Za ocjenu 5 student treba pokazati da razumije:

- modele
- relacije
- API rute
- frontend povezivanje s backendom
- rad s formama
- rad s tabličnim prikazima
- razliku između frontend i backend pretrage
- razliku između frontend i backend paginacije

## 12. Grid system, responsive i UX

Ovo se također gleda kod ocjenjivanja.

Student treba pokazati da razumije:

- raspored elemenata preko `v-container`, `v-row`, `v-col`
- kako elementi izgledaju na manjim i većim ekranima
- da stranice nisu razbijene na mobitelu ili manjem laptopu

Ocjenjuje se vizualna urednost:

- forme su pregledne
- gumbi su na smislenim mjestima
- tablice su čitljive
- stranice imaju smislen raspored

Ocjenjuje se i UX:

- jasno je kako dodati zapis
- jasno je kako urediti zapis
- jasno je kako obrisati zapis
- korisnik dobije potvrdu prije brisanja
- flow kroz aplikaciju je logičan i jednostavan

## 13. Dodatne funkcionalnosti

Ako student želi bolji projekt, može dodati:

- `debounce` pretragu preko `setTimeout`
- filtere
- sortiranje
- snackbar poruke nakon spremanja ili brisanja
- validaciju forme
- pregled povezanih zapisa
- više relacija među tablicama
- bolji prikaz detalja jednog zapisa

To nije nužno za prolaz, ali podiže kvalitetu projekta.

## 14. Preporučeni redoslijed rada

Preporučeni redoslijed rada:

1. Osmisliti temu projekta.
2. Napraviti plan tablica.
3. Definirati relacije među tablicama.
4. Napraviti modele.
5. Napraviti bazu i migracije.
6. Napraviti backend CRUD rute.
7. Testirati backend kroz Postman.
8. Napraviti frontend tablične prikaze.
9. Napraviti forme za dodavanje i uređivanje.
10. Povezati frontend s backendom.
11. Napraviti dashboard početnu stranicu.
12. Dodati pretragu.
13. Dodati paginaciju.
14. Dodati filtere, validaciju i ostale dodatne funkcionalnosti ako ima vremena.

## 15. Napomena za ocjenjivanje

Ocjena ne ovisi samo o količini koda.

Gleda se:

- radi li projekt
- je li baza smisleno napravljena
- postoje li relacije
- rade li CRUD operacije
- je li frontend povezan s backendom
- je li kod uredan i razumljiv
- ima li projekt smislen flow
- razumije li student što je napravio
- je li aplikacija vizualno uredna
- je li aplikacija ugodna za korištenje

## 16. Zaključak

Ovaj template nije gotov studentski projekt, nego osnova.

Student treba:

- promijeniti temu
- prilagoditi tablice
- prilagoditi modele
- prilagoditi rute
- prilagoditi frontend stranice

Cilj je da student pokaže da zna napraviti **cijeli mali informacijski sustav**:

- baza
- backend
- frontend
- CRUD
- relacije
- dashboard
- pretraga
- paginacija

Ako student napravi samo minimum i sve radi ispravno, to je dovoljno za prolaz.
Ako uz to napravi uredniji projekt s dodatnim funkcionalnostima, to podiže ocjenu.
