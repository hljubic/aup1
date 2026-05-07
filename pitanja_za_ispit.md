# Pitanja za ispit

Ova pitanja služe za provjeru razumijevanja projekta. Naglasak je na tome da student zna pokrenuti projekt, objasniti kod i napraviti osnovnu izmjenu.

## Pokretanje projekta

| # | Pitanje | Očekivani odgovor |
|---|---|---|
| 1 | Što student mora napraviti ako obriše `.venv`? | Mora ponovno napraviti virtualno okruženje, aktivirati ga i instalirati backend pakete iz `requirements.txt`. |
| 2 | Što student mora napraviti ako obriše `aup-frontend/node_modules`? | Mora u frontend folderu ponovno pokrenuti `npm install`. |
| 3 | Zašto se `.venv` i `node_modules` ne šalju na GitHub? | To su generirani folderi koji se mogu ponovno napraviti iz `requirements.txt` i `package.json`. |
| 4 | Koje datoteke moraju ostati u projektu da bi se paketi mogli ponovno instalirati? | Za backend je bitan `requirements.txt`, a za frontend `package.json` i `package-lock.json`. |
| 5 | Kako bi student provjerio radi li backend bez frontenda? | Može otvoriti API rutu u browseru ili poslati zahtjev kroz Postman. |
| 6 | Kako bi student provjerio radi li frontend API poziv? | Može otvoriti Developer Tools i pogledati `Network` ili `Console`. |

## Migracije i baza

| # | Pitanje | Očekivani odgovor |
|---|---|---|
| 7 | Što je migracija? | Migracija je skripta koja promjene iz modela prenosi u strukturu baze podataka. |
| 8 | Što radi `flask db init`? | Inicijalizira migracije i napravi `migrations` folder. |
| 9 | Što radi `flask db migrate`? | Napravi novu migracijsku skriptu na temelju promjena u modelima. |
| 10 | Što radi `flask db upgrade`? | Primjenjuje migracije na bazu podataka i stvarno mijenja tablice. |
| 11 | Zašto nije dovoljno samo napisati novu klasu u `models.py`? | Zato što se promjena neće pojaviti u bazi dok se ne napravi i ne pokrene migracija. |
| 12 | Što znači `primary_key=True`? | Označava glavni identifikator zapisa u tablici. |
| 13 | Što znači `nullable=False`? | Znači da polje u bazi ne smije biti prazno. |
| 14 | Što je strani ključ? | Strani ključ povezuje zapis iz jedne tablice sa zapisom iz druge tablice. |
| 15 | Kako je u ovom projektu `Kolegij` povezan s `Profesor`? | `Kolegij` ima `nositelj_id`, koji pokazuje na `id` profesora. |

## Flask backend

| # | Pitanje | Očekivani odgovor |
|---|---|---|
| 16 | Što je ruta u Flasku? | Ruta je URL endpoint koji izvršava određenu Python funkciju. |
| 17 | Što znači `@app.route('/profesori', methods=['GET'])`? | Ta funkcija odgovara na `GET` zahtjev prema `/profesori`. |
| 18 | Koja HTTP metoda služi za dodavanje novog zapisa? | Za dodavanje se koristi `POST`. |
| 19 | Koja HTTP metoda služi za uređivanje zapisa? | Za uređivanje se koristi `PUT`. |
| 20 | Koja HTTP metoda služi za brisanje zapisa? | Za brisanje se koristi `DELETE`. |
| 21 | Što radi `request.get_json()`? | Čita JSON podatke koje je frontend ili Postman poslao u bodyju zahtjeva. |
| 22 | Što radi `Profesor.query.all()`? | Dohvaća sve zapise iz tablice profesora. |
| 23 | Što radi `Profesor.query.filter_by(id=id).first()`? | Dohvaća prvog profesora koji ima zadani `id`. |
| 24 | Što radi `db.session.add(...)`? | Dodaje novi objekt u trenutnu baznu sesiju. |
| 25 | Što radi `db.session.commit()`? | Sprema promjene u bazu podataka. |
| 26 | Što radi `db.session.delete(...)`? | Označava zapis za brisanje iz baze. |
| 27 | Što radi metoda `to_dict()` u modelu? | Pretvara objekt iz baze u običan dictionary koji se može vratiti kao JSON. |
| 28 | Što radi `CORS(app)`? | Dopušta frontendu i backendu da komuniciraju iako rade na različitim portovima. |

## CRUD

| # | Pitanje | Očekivani odgovor |
|---|---|---|
| 29 | Objasni što znači CRUD. | CRUD znači dodavanje, čitanje, uređivanje i brisanje podataka. |
| 30 | Što se treba dogoditi u bazi nakon `POST /profesori`? | U tablicu `profesori` treba se dodati novi zapis. |
| 31 | Što se treba dogoditi u bazi nakon `PUT /profesori/1`? | Trebaju se promijeniti podaci profesora s ID-em `1`. |
| 32 | Što se treba dogoditi u bazi nakon `DELETE /profesori/1`? | Profesor s ID-em `1` treba biti obrisan iz baze. |
| 33 | Zašto za kolegij koristimo dropdown za `nositelj_id`? | Zato da korisnik izabere postojećeg profesora umjesto da ručno upisuje ID. |

## Vue frontend

| # | Pitanje | Očekivani odgovor |
|---|---|---|
| 34 | Čemu služi `v-model`? | Povezuje input polje s varijablom u Vue komponenti. |
| 35 | Čemu služi `v-if`? | Uvjetno prikazuje ili skriva dio templatea. |
| 36 | Čemu služi `v-for`? | Ponavlja elemente na temelju liste podataka. |
| 37 | Što znači `@click`? | Poziva funkciju kada korisnik klikne na element. |
| 38 | Što je `ref`? | `ref` je reaktivna varijabla za jednu vrijednost. |
| 39 | Što je `reactive`? | `reactive` je reaktivni objekt s više povezanih polja. |
| 40 | Kada bi koristio `reactive` umjesto `ref`? | Kada imam objekt, na primjer cijelu formu s više polja. |
| 41 | Što radi `onMounted()`? | Pokreće kod nakon što se komponenta učita na stranicu. |
| 42 | Što radi `fetch()`? | Šalje HTTP zahtjev prema backend API-ju. |
| 43 | Zašto kod `POST` i `PUT` koristimo `JSON.stringify(...)`? | Zato što objekt iz JavaScripta treba pretvoriti u JSON tekst prije slanja backendu. |
| 44 | Što radi `router.push(...)`? | Prebacuje korisnika na drugu rutu u frontend aplikaciji. |

## Tablice i forme

| # | Pitanje | Očekivani odgovor |
|---|---|---|
| 45 | Čemu služi `v-data-table`? | Služi za tablični prikaz liste podataka. |
| 46 | Što predstavljaju `headers` u tablici? | Predstavljaju stupce tablice. |
| 47 | Što predstavljaju `items` u tablici? | Predstavljaju podatke koji se prikazuju u redovima tablice. |
| 48 | Što se dogodi kada korisnik klikne `Dodaj`? | Frontend ga vodi na formu za dodavanje novog zapisa. |
| 49 | Što se dogodi kada korisnik klikne `Uredi`? | Frontend ga vodi na formu za uređivanje i dohvaća postojeće podatke. |
| 50 | Kako se forma za uređivanje popuni postojećim podacima? | Frontend pozove API za jedan zapis i dobivene podatke stavi u formu. |
| 51 | Zašto koristimo isti page za dodavanje i uređivanje? | Zato što forma ima ista polja, samo se razlikuje metoda slanja podataka. |
| 52 | Kako frontend zna kojeg profesora treba urediti? | ID profesora nalazi se u URL ruti, na primjer `/profesori/1/uredi`. |

## Pretraga i paginacija

| # | Pitanje | Očekivani odgovor |
|---|---|---|
| 53 | Što je frontend pretraga? | Frontend dohvaća podatke i filtrira ih u browseru. |
| 54 | Što je backend pretraga? | Frontend šalje pojam backendu, a backend vraća samo pronađene rezultate. |
| 55 | Koja je razlika između frontend i backend pretrage? | Kod frontend pretrage filtrira browser, a kod backend pretrage filtrira baza preko backend API-ja. |
| 56 | Što je paginacija? | Paginacija dijeli veliku listu podataka na stranice. |
| 57 | Što je frontend paginacija? | Frontend dobije sve podatke pa ih sam dijeli na stranice. |
| 58 | Što je backend paginacija? | Backend vraća samo podatke za traženu stranicu. |
| 59 | Zašto je backend paginacija bolja kada imamo puno podataka? | Zato što se ne učitava cijela tablica odjednom. |
| 60 | Što znači `page`? | Označava koju stranicu podataka korisnik traži. |
| 61 | Što znači `per_page`? | Označava koliko zapisa se prikazuje po stranici. |

## Dashboard i GitHub

| # | Pitanje | Očekivani odgovor |
|---|---|---|
| 62 | Što je dashboard u ovom projektu? | Početna stranica koja prikazuje osnovne informacije iz baze. |
| 63 | Koje osnovne informacije može prikazati dashboard? | Može prikazati broj zapisa, prosjeke, zadnje dodane podatke ili slične sažetke. |
| 64 | Kako bi backend mogao vratiti broj profesora? | Može napraviti query koji broji zapise u tablici `profesori`. |
| 65 | Zašto frontend i backend trebaju biti u dva odvojena repozitorija? | Zato što su to dvije odvojene aplikacije s različitim paketima i načinom pokretanja. |
| 66 | Što treba poslati na mail prije ispitnog roka? | Treba poslati GitHub link za backend i GitHub link za frontend. |

## Praktični zadaci

| # | Zadatak | Očekivani rezultat |
|---|---|---|
| 67 | Obriši `.venv` i ponovno postavi backend okruženje. | Student treba napraviti virtualno okruženje, aktivirati ga i instalirati pakete iz `requirements.txt`. |
| 68 | Obriši `aup-frontend/node_modules` i ponovno instaliraj frontend pakete. | Student treba u frontend folderu pokrenuti `npm install`. |
| 69 | Kreiraj bazu podataka i pokreni migracije od početka. | Student treba napraviti bazu u `phpMyAdmin`, zatim pokrenuti `flask db init`, `flask db migrate` i `flask db upgrade`. |
| 70 | U Postmanu dodaj, uredi i obriši jednog profesora. | Student treba znati koristiti `POST`, `PUT` i `DELETE` API rute. |
| 71 | Objasni što se događa od klika na gumb `Spremi` do spremanja podatka u bazu. | Klik pozove frontend funkciju, ona šalje API zahtjev, backend primi podatke, spremi ih u bazu i vrati odgovor. |

## Brza provjera razumijevanja

| # | Pitanje | Očekivani odgovor |
|---|---|---|
| 72 | Što bi se dogodilo da u formi nema `v-model`? | Input ne bi bio povezan s podacima u komponenti. |
| 73 | Što bi se dogodilo da se ne pozove `db.session.commit()`? | Promjene se ne bi spremile u bazu. |
| 74 | Što bi se dogodilo da frontend zove krivi port? | API poziv ne bi došao do backend aplikacije. |
| 75 | Što bi se dogodilo da `CORS` nije uključen? | Browser bi mogao blokirati zahtjev između frontenda i backenda. |
| 76 | Kako bi znao je li greška na backendu ili frontendu? | Backend se provjeri u Postmanu ili browseru, a frontend kroz `Console` i `Network` tab. |
