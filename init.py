from flask import Flask, render_template, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
import os
import sys


# if __name__ == "__main__":
project_dir = os.path.dirname(os.path.abspath(__file__))
db_sql_lite = "sqlite:///{}".format(os.path.join(project_dir, "db_dev.db"))
db_mariadb = "mariadb+mariadbconnector://univesp:univesp@127.0.0.1:3306/pi2025_1"

# descomentar para alternar entre um e outro
# produção
# db_atual = db_mariadb

# desenvolvimento
db_atual = db_sql_lite

# app = Flask(__name__)
nomeApp = "Appy"
# global app
app = Flask(nomeApp)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = db_atual
# global db
db = SQLAlchemy(app)
