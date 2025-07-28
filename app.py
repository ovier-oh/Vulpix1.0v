from flask import Flask, request, jsonify
import os 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)



# Configguracion de la aplicacion 
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

app.config['JWT_SECRET_KEY'] = "super-secreta"
jwt = JWTManager(app)


bcrypt = Bcrypt(app)

# Ejecuta esto en un shell de Python o al inicio de tu app
with app.app_context():
    db.drop_all()  # Elimina todas las tablas
    db.create_all()  # Crea las tablas con el nuevo esquema


# Modelo de Usuario 
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    contraseña = db.Column(db.String(120), nullable=False)


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

@app.route("/login", methods=["POST"])
def login():
    nombre = request.json.get("nombre")
    contraseña = request.json.get("contraseña")
    
    usuario = Usuario.query.filter_by(nombre = nombre).first() 

    if not nombre or not bcrypt.check_password_hash(usuario.contraseña,contraseña): 
        return jsonify({"error": "Credenciales Invalidas"}), 401 
    
    # Genera un token JWT 
    token = create_access_token(identity=nombre)
    return jsonify({"token": token})

# Rutaa protegisda 
@app.route("/protegido", methods=["GET"])
@jwt_required()
def protegido():
    usuario_actual = get_jwt_identity() 
    return jsonify({"mensaje": f"Bienvenido {usuario_actual} (ruta protegida)"})

@app.route('/registro', methods=['POST'])
def registro():
    data = request.json
    if not data or 'nombre' not in data or 'contraseña' not in data:
        return jsonify({"error": "Nombre y contraseña son requeridos"}), 400

    nombre = data['nombre']
    contraseña = data['contraseña']  # ¡Campo correcto!

    contraseña_hash = bcrypt.generate_password_hash(contraseña).decode('utf-8')
    nuevo_usuario = Usuario(nombre=nombre, contraseña=contraseña_hash)  # ¡Consistente!
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"mensaje": "Usuario registrado"}), 201

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Solicitud mal formada"}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Recurso no encontrado"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

