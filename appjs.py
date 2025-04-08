from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify, Response
import sys
import os
from interfaces import clientes_sql, clientes_sqla
from init import app

id_clientes = 0
tClientes = clientes_sqla()

# def resposta(status, dados={}):
#     # data = {"status": "success", "some_key": "some_value"}
#     response = app.response_class(
#         response=json.dumps(dados),
#         status=200,
#         mimetype='application/json'
#     )
#     return response

# mdbCFG = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'univesp',
#     'password': 'univesp',
#     'database': 'pi2025_1'
# }


# @app.route('/', methods=['POST', 'GET'])
@app.route('/')
def home():
    return render_template('indexjs.html')


@app.route('/api/clientes', methods=['GET'])
def clientesGet():
    return tClientes.pegarTodos()

    # # connection for MariaDB
    # conn = mariadb.connect(**mdbCFG)
    # # create a connection cursor
    # cur = conn.cursor()
    # # execute a SQL statement
    # try:
    #     cur.execute("SELECT * FROM clientes")
    #     conn.commit()
    # except:
    #     print("erro ao GET")
    #     return {}, 500

    # # serialize results into JSON
    # row_headers = [x[0] for x in cur.description]
    # rv = cur.fetchall()
    # json_data = []
    # for result in rv:
    #     json_data.append(dict(zip(row_headers, result)))
    # # return the results!
    # # return json.dumps(json_data)
    # # return resposta(200, json.dumps(json_data))
    # return json.dumps(json_data), 200


@app.route('/api/clientes', methods=['POST'])
def clientesPost():
    # pegando nome
    nome = request.json["nome"]

    return tClientes.adicionar(nome)

    # # connection for MariaDB
    # conn = mariadb.connect(**mdbCFG)
    # # create a connection cursor
    # cur = conn.cursor()
    # # execute a SQL statement
    # # print(f"insert into clientes (nome) VALUES ('{nome}');")
    # try:
    #     cur.execute(f"INSERT INTO clientes (nome) VALUES ('{nome}');")
    #     conn.commit()
    # except:
    #     print("erro ao POST")
    #     return {}, 500

    # return {}, 201


@app.route('/api/clientes', methods=['DELETE'])
def clientesDel():
    # pegando nome
    nome = request.json["nome"]

    return tClientes.deletar(nome)

    # # connection for MariaDB
    # conn = mariadb.connect(**mdbCFG)
    # # create a connection cursor
    # cur = conn.cursor()
    # # print(f"delete from clientes WHERE nome='{nome}';")
    # # execute a SQL statement
    # cur.execute(f"DELETE FROM clientes WHERE nome='{nome}';")
    # conn.commit()

    # return {}, 200


def rodar():
    # port = int(os.environ.get('PORT', 5000))
    # app.run(debug=True, host='0.0.0.0', port=port)
    # app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run(debug=True, host='127.0.0.1', port=5000)
    app.run(debug=True, host='localhost', port=5000)
    # app.run()


if __name__ == "__main__":

    if (len(sys.argv) > 1):
        if (sys.argv[1] == "sql"):
            tClientes = clientes_sql()

    tClientes.criarTabela()
    rodar()
# # connection for MariaDB
# conn = mariadb.connect(**mdbCFG)
# # create a connection cursor
# cur = conn.cursor()
# # execute a SQL statement
# try:
#     cur.execute("select * from clientes")
#     conn.commit()

#     # cur.execute("""SELECT COUNT(clientes)
#     # # FROM
#     # #    information_schema.TABLES
#     # # WHERE
#     # #    TABLE_SCHEMA LIKE 'nome'""")
# except:
#     cur.execute("""CREATE TABLE clientes (
#     nome varchar(255))""")
#     print("criando clientes")
#     conn.commit()

#     cur.execute("""SELECT COUNT(clientes)
# FROM
#    information_schema.TABLES
# WHERE
#    TABLE_SCHEMA LIKE 'nome'""")
# resultado = cur.fetchall()
# if not resultado:
# cur.execute("""CREATE TABLE clientes (
# clientes_id int,
# nome varchar(255),
# sobrenome varchar(255),
# endereço varchar(255),
# cidade varchar(255)
# )""")
# cur.execute("""CREATE TABLE clientes (
# nome varchar(255),
# )""")
