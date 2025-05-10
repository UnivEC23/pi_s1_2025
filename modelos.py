from dataclasses import dataclass
from init import db
from datetime import datetime  # Importe o módulo datetime


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


@dataclass
class Comentario(db.Model):
    id: int
    autor: str
    texto: str
    data_criacao: datetime

    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    autor = db.Column(db.String(80), nullable=False)
    texto = db.Column(db.String(500), nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Comentario Autor: {}>".format(self.autor)