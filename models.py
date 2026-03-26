from sqlalchemy.orm import backref

from extensions import db

class Profesor(db.Model):
    __tablename__ = "profesori"

    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(30), nullable=False) # Ctrl + D za duplicate retka
    prezime = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    titula = db.Column(db.String(20), nullable=True) # ovo polje ne moramo unositi

    # ovo je opcionalno sada, ali poželjno, da dodamo relaciju i s druge strane
    # u model Profesor dodajemo iduće:
    kolegiji = db.relationship("Kolegij", backref="nositelj", lazy=True)
    # za DZ istražite što je "lazy loading"

class Kolegij(db.Model):
    __tablename__ = "kolegiji"

    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String(60), nullable=False)
    ects = db.Column(db.Integer, nullable=False)
    semestar = db.Column(db.Integer, nullable=True)

    nositelj_id = db.Column(db.Integer, db.ForeignKey("profesori.id"), nullable=True)

