from app import create_app
from app.extensions import db

app = create_app()
# Ejecuta esto en un shell de Python o al inicio de tu app
with app.app_context():
    db.drop_all()  # Elimina todas las tablas
    db.create_all()  # Crea las tablas con el nuevo esquema