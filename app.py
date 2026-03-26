from flask import Flask
from extensions import db, migrate
from models import Profesor, Kolegij

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:csdigital@localhost/aup1"
# Kod mene je password csdigital, kod vas treba ostati prazno.
db.init_app(app)
migrate.init_app(app, db)

# mozemo root rutu
@app.route('/')
def index():
    return "početna"

@app.route('/novi_kolegij/<naziv>/<ects>') # to su dva required polja
def novi_kolegij(naziv, ects):

    kolegij = Kolegij(naziv=naziv, ects=ects)
    db.session.add(kolegij)
    db.session.commit()

    return "dodano"

# Samostalno napraviti rutu za ispis svih kolegija.
# ovo je najosnovniji primjer, a primjere bolje prakse ćemo proći na idućim vježbama.
# idemo još samo dodati sve ovo na git, ostali su nam folder migrations i ja cu dodati ovaj video.txt
# prvo ću promjeniti ime fajla kroz terminal

# prvo da pokrenemo server
app.run(debug=True)