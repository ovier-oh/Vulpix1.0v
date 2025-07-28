from flask import Flask
from .config import Config
from .extensions import db, bcrypt, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializar extensiones
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    # Registrar blueprints
    from .routes.auth import auth_bp
    from .routes.public import public_bp
    from .routes.protected import protected_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(public_bp)
    app.register_blueprint(protected_bp)
    
    # Registrar manejadores de error (importación corregida)
    from .utils.error_handlers import register_error_handlers
    register_error_handlers(app)
    
    return app