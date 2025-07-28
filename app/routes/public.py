from flask import Blueprint, jsonify, request

public_bp = Blueprint('public', __name__)

@public_bp.route('/')
def hola_mundo():
    return jsonify({"mensaje": "Hola Mundo desde Flask"}), 200

@public_bp.route('/saludar', methods=['POST'])
def saludar():
    nombre = request.json.get("nombre")
    if not nombre:
        return jsonify({"error": "Nombre es requerido"}), 400
    return jsonify({"mensaje": f"Hola, {nombre}!"}), 200