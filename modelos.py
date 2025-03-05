from dataclasses import dataclass
from init import db


@dataclass
class Clientes(db.Model):
    nome: str

# nome não pode ser primaria mas é só pelo teste
    nome = db.Column(db.String(255), unique=False,
                     nullable=False, primary_key=True)

    def __repr__(self):
        return "<Nome: {}>".format(self.nome)
