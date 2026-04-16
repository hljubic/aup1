from flask import Flask, jsonify, request
from extensions import db, migrate
from models import Profesor, Kolegij, Ucionica

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost/aup1"
db.init_app(app)
migrate.init_app(app, db)


# mozemo root rutu
@app.route('/')
def index():
    return "početna"


@app.route('/novi_kolegij/<naziv>/<ects>')  # to su dva required polja
def novi_kolegij(naziv, ects):
    kolegij = Kolegij(naziv=naziv, ects=ects)
    db.session.add(kolegij)
    db.session.commit()

    return "dodano"


@app.route('/nova_ucionica/<oznaka>/<kat>/<kapacitet>')
def nova_ucionica(oznaka, kat, kapacitet):
    ucionica = Ucionica(oznaka=oznaka, kat=kat, kapacitet=kapacitet)

    db.session.add(ucionica)
    db.session.commit()

    return "Dodana učionica."

@app.route('/ucionice')
def ucionice():
    ucionice = Ucionica.query.all()

    return jsonify([u.to_dict() for u in ucionice])

# 4. zadatak - app.py
# 4.1. napraviti rutu za dodavanje nove učionice (primjer novi_kolegij)
# 4.2. napraviti rutu za ispis svih učionica.

# Samostalno napraviti rutu za ispis svih kolegija.
# ovo je najosnovniji primjer, a primjere bolje prakse ćemo proći na idućim vježbama.
# idemo još samo dodati sve ovo na git, ostali su nam folder migrations i ja cu dodati ovaj video.txt
# prvo ću promjeniti ime fajla kroz terminal

# prvo da pokrenemo server

@app.route('/profesori', methods=['GET'])
def profesori():
    profesori = Profesor.query.all()

    return [profesor.to_dict() for profesor in profesori]

# GET /profesori/:ID
# Napraviti GET rutu za profesore ali po točno nekom ID-u
# Točnije dohvat samo jednog profesora.

@app.route('/profesori/<id>', methods=['GET'])
def profesor(id):
    profesor = Profesor.query.filter_by(id=id).first()

    return profesor.to_dict()


@app.route('/profesori', methods=['POST'])
def novi_profesor():
    data = request.get_json()

    profesor = Profesor(
        ime=data.get('ime'),
        prezime=data.get('prezime'),
        email=data.get('email'),
        titula=data.get('titula')
    )

    db.session.add(profesor)
    db.session.commit()

    return "Uspješno dodano."

@app.route('/profesori/<id>', methods=['DELETE'])
def izbrisi_profesora(id):
    profesor = Profesor.query.filter_by(id=id).first()

    db.session.delete(profesor)
    db.session.commit()

    return "Izbrisano"


# Napraviti UPDATE metodu za profesore
# PUT /profesori/<id>
# Prvo treba dohvatiti profesora po ID-u
# Nakon toga ide isti kod kao kod dodavanja - ali treba koristiti update dio

@app.route('/profesori/<id>', methods=['PUT'])
def uredi_profesora(id):
    profesor = Profesor.query.filter_by(id=id).first()

    data = request.get_json()

    profesor.ime = data.get('ime')
    profesor.prezime = data.get('prezime')
    profesor.email = data.get('email')
    profesor.titula = data.get('titula')

    db.session.commit()

    return "Napravljene promjene"

app.run(debug=True, port=5000)









