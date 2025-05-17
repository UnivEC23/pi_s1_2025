from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify, Response
import sys
import os
from interfaces import clientes_sql, clientes_sqla
from init import app, db
from modelos import Comentario 
from sqlalchemy import desc  


id_clientes = 0
tClientes = clientes_sqla()

login_usuario = "user"
login_senha = "pass"


# ---------paginas ativas--------------------------

@app.route('/', methods=['POST', 'GET'])
def home():
    comentarios = pegar_comentarios()
    if request.method == 'GET':
        return render_template('indexjs.html', comentarios=comentarios)
    elif request.method == 'POST':
        novo = request.form
        if not novo.get("nome") or not novo.get("email") or not novo.get("solicit"):
            return render_template('indexjs.html', form_error="Por favor, preencha todos os campos do formulário.", comentarios=comentarios)        

        tClientes.adicionar(novo.get("nome"), novo.get("email"), novo.get("solicit"))
        return render_template('indexjs.html', comentarios=comentarios)


@app.route('/clientes', methods=['POST'])
def clientes():
    login = request.form
    if not login.get("username") or not login.get("password"):
        return render_template('indexjs.html', login_error="Por favor, preencha todos os campos do login.", comentarios=pegar_comentarios())

    if login.get("username") == login_usuario and login.get("password") == login_senha:
        return render_template('clientes.html')
    else:
        return render_template('indexjs.html', login_error="Usuário ou senha incorretos.", comentarios=pegar_comentarios())

# adicionado para testes sem login
@app.route('/clientes', methods=['GET'])
def clientesget():
    return render_template('clientes.html')


# --------api clientes------------------

@app.route('/api/clientes', methods=['GET'])
def clientesGet():
    return tClientes.pegarTodos()

@app.route('/api/clientes', methods=['POST'])
def clientesPost():
    # pegando nome
    nome = request.json["nome"]
    email = request.json["email"]
    solicit = request.json["solicit"]

    # print(nome, email, solicit)

    return tClientes.adicionar(nome, email, solicit)


@app.route('/api/clientes', methods=['DELETE'])
def clientesDel():
    # pegando nome
    nome = request.json["nome"]

    return tClientes.deletar(nome)

# --------api comentarios-----------------

@app.route('/api/comentarios', methods=['POST'])
def adicionar_comentario():
    try:
        data = request.get_json()
        autor = data.get('autor')
        texto = data.get('texto')

        if not autor or not texto:
            return jsonify({'erro':'Autor e texto são obrigatórios.'})

        novo_comentario = Comentario(autor=autor, texto=texto)
        db.session.add(novo_comentario)
        db.session.commit()

        return jsonify({'mensagemok':'Comentário adicionado com sucesso!'})
    except Exception as e:
      
        return jsonify({'mensagemoff':'Erro ao adicionar comentário.'+e})
# ------------------------------

def rodar():
    # port = int(os.environ.get('PORT', 5000))
    # app.run(debug=True, host='0.0.0.0', port=port)
    # app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run(debug=True, host='127.0.0.1', port=5000)
    app.run(debug=True, host='localhost', port=5000)
    # app.run()


def pegar_comentarios():
    with app.app_context(): 
        try:
            comentarios = Comentario.query.order_by(desc(Comentario.data_criacao)).limit(3).all()
            return comentarios
        except Exception as e:
            print("Erro ao buscar comentários:", e)
            return [] 


if __name__ == "__main__":

    if (len(sys.argv) > 1):
        if (sys.argv[1] == "sql"):
            tClientes = clientes_sql()

    tClientes.criarTabela()
    with app.app_context():
        db.create_all()  # crias as tabelas
    rodar()