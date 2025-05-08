from flask import jsonify
# from datetime import datetime
# from flask.json import JSONEncoder
from abc import ABC, abstractmethod
import json
import mariadb
from modelos import Clientes
from init import app, db


# pode não ser necessário
# """ajuda a serializar mes/ano"""
# class CustomJSONEncoder(JSONEncoder):

#     def default(o):
#         if type(o) == datetime.timedelta:
#             return str(o)
#         if type(o) == datetime.datetime:
#             return o.isoformat()
#         return super().default(o)

# app.json_encoder = CustomJSONEncoder

mdbCFG = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'univesp',
    'password': 'univesp',
    'database': 'pi2025_1'
}


class iClientes(ABC):
    @abstractmethod
    def criarTabela(self):
        # raise NotImplementedError
        pass

    @abstractmethod
    def pegarTodos(self):
        pass

    @abstractmethod
    def deletar(self):
        pass

    @abstractmethod
    def adicionar(self):
        pass


# implementação usando sql puro


class clientes_sql(iClientes):
    def __init__(self) -> None:
        # self.id = id
        # self.nome = nome
        pass

    def criarTabela(self):
        # connection for MariaDB
        conn = mariadb.connect(**mdbCFG)
        # create a connection cursor
        cur = conn.cursor()
        # execute a SQL statement
        try:
            cur.execute("select * from clientes")
            conn.commit()

            # cur.execute("""SELECT COUNT(clientes)
            # # FROM
            # #    information_schema.TABLES
            # # WHERE
            # #    TABLE_SCHEMA LIKE 'nome'""")
        except:
            cur.execute("""CREATE TABLE clientes (
                nome varchar(255))""")
            print("criando clientes")
            conn.commit()

    def pegarTodos(self):
        conn = mariadb.connect(**mdbCFG)
        # create a connection cursor
        cur = conn.cursor()
        # execute a SQL statement
        try:
            cur.execute("SELECT * FROM clientes")
            conn.commit()
        except Exception as e:
            print("erro ao GET")
            print(e)
            return {}, 500
            # serialize results into JSON

        row_headers = [x[0] for x in cur.description]
        rv = cur.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        # return the results!
        # return json.dumps(json_data)
        # return resposta(200, json.dumps(json_data))
        return json.dumps(json_data), 200

    def deletar(self, nome):
        # connection for MariaDB
        conn = mariadb.connect(**mdbCFG)
        # create a connection cursor
        cur = conn.cursor()
        # pegando nome
        # nome = request.json["nome"]
        # print(f"delete from clientes WHERE nome='{nome}';")
        # execute a SQL statement
        try:
            cur.execute(f"DELETE FROM clientes WHERE nome='{nome}';")
            conn.commit()
            return {}, 200
        except Exception as e:
            print("erro ao delete")
            print(e)
            return {}, 500

    def adicionar(self, nome: str, email:str, solicit:str):
        # connection for MariaDB
        conn = mariadb.connect(**mdbCFG)
        # create a connection cursor
        cur = conn.cursor()
        # pegando nome
        # nome = request.json["nome"]
        # print(f"delete from clientes WHERE nome='{nome}';")
        # execute a SQL statement
        try:
            cur.execute(f"INSERT INTO clientes (nome) VALUES ('{nome}');")
            conn.commit()
            return {}, 201
        except Exception as e:
            print("erro ao delete")
            print(e)
            return {}, 500


# implementação usando sqlAlchemy


class clientes_sqla(iClientes):
    def __init__(self) -> None:
        # self.id = id
        # self.nome = nome
        pass

    def criarTabela(self):
        with app.app_context():
            db.create_all()

    def pegarTodos(self):
        try:
            clientes = Clientes.query.all()

            return jsonify(clientes), 200
        except Exception as e:
            print("erro ao GET")
            print(e)
            return {}, 500

    def deletar(self, nome):
        try:
            # se filtrar pelo primeiro---
            # cliente = Clientes.query.filter_by(nome=nome).first()
            # db.session.delete(cliente)
            # ---

            # se pegar todos----
            clientes = Clientes.query.filter_by(nome=nome).all()
            for c in clientes:
                db.session.delete(c)
            # ----

            db.session.commit()
            return {}, 200
        except Exception as e:
            print("erro ao delete")
            print(e)
            return {}, 500

    def adicionar(self, nome: str, email:str, solicit:str):
        try:
            cliente = Clientes(nome=nome, email=email, solicit=solicit)
            db.session.add(cliente)
            db.session.commit()
            return {}, 201
        except Exception as e:
            print("erro ao delete")
            print(e)
            return {}, 500
