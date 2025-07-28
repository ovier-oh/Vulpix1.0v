from flask import Flask, request, jsonify
import os 
from flask_sqlalchemy import SQLAlchemy

# Configguracion de la aplicacion 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Modelo de Usuario 
class Usuario(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)

# Configuracion de la base de datos 
@app.route("/")
def hola_mundo():
    return "Hola Mundo desde Flask"

@app.route("/saludar", methods=["POST"])
def saludar():
    nombre = request.json.get("nombre")
    return jsonify({"mensaje": f"Hola, {nombre}!"})

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    nombre = request.json.get("nombre")
    if not nombre: 
        return jsonify({"error": "Falta el nombre"}), 400 
    
    nuevo_usuario = Usuario(nombre=nombre)
    db.session.add(nuevo_usuario)
    db.session.commit() 

    return jsonify({"mensaje": f"Usuario {nombre} creado!"}), 201 



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

