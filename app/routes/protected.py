from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..extensions import db
from ..models import Usuario

protected_bp = Blueprint('protected', __name__)

@protected_bp.route('/protegido', methods=['GET'])
@jwt_required()
def protegido():
    current_user = get_jwt_identity()
    return jsonify({"mensaje": f"Bienvenido {current_user} (ruta protegida)"}), 200