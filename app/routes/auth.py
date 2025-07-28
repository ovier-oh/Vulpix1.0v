from flask import Blueprint, request, jsonify
from ..extensions import bcrypt, db
from ..models import Usuario
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/registro', methods=['POST'])
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


@auth_bp.route('/login', methods=['POST'])
def login():
    nombre = request.json.get("nombre")
    contraseña = request.json.get("contraseña")
    
    usuario = Usuario.query.filter_by(nombre = nombre).first() 

    if not nombre or not bcrypt.check_password_hash(usuario.contraseña,contraseña): 
        return jsonify({"error": "Credenciales Invalidas"}), 401 
    
    # Genera un token JWT 
    token = create_access_token(identity=nombre)
    return jsonify({"token": token})
    