from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify, Response
import sys
import os
from interfaces import clientes_sql, clientes_sqla
from init import app

id_clientes = 0
tClientes = clientes_sqla()

#---------paginas ativas--------------------------

@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('indexjs.html')




@app.route('/clientes', methods=['POST'])
def clientes():
    return render_template('clientes.html')


#adicionado para testes sem login
@app.route('/clientes', methods=['GET'])
def clientesget():
    return render_template('clientes.html')



#--------api clientes------------------

@app.route('/api/clientes', methods=['GET'])
def clientesGet():
    return tClientes.pegarTodos()

@app.route('/api/clientes', methods=['POST'])
def clientesPost():
    # pegando nome
    nome = request.json["nome"]

    return tClientes.adicionar(nome)



@app.route('/api/clientes', methods=['DELETE'])
def clientesDel():
    # pegando nome
    nome = request.json["nome"]

    return tClientes.deletar(nome)

#------------------------------

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
