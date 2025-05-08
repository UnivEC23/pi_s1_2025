from dataclasses import dataclass
from init import db


@dataclass
class Clientes(db.Model):
    id:int
    nome: str
    email: str
    solicit: str

    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), unique=False,
                     nullable=True, primary_key=False)
    email = db.Column(db.String(80), unique=False,
                     nullable=True, primary_key=False)
    solicit = db.Column(db.String(500), unique=False,
                     nullable=True, primary_key=False)
    

    def __repr__(self):
        return "<Nome: {}>".format(self.nome)
