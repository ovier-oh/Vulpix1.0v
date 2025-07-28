# 🔒 API de Autenticación Flask con JWT y SQLite

API RESTful para autenticación de usuarios usando Flask, JWT (JSON Web Tokens) y SQLite como base de datos.

## 🚀 Características principales
- Registro y login de usuarios
- Protección de rutas con JWT
- Almacenamiento seguro de contraseñas (hashing con bcrypt)
- Manejo de errores estructurado
- Documentación completa de endpoints

## 📦 Requisitos
- Python 3.8+
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- Flask-Bcrypt

## 🛠️ Instalación
```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/flask-jwt-auth.git
cd flask-jwt-auth

# Crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

⚙️ Configuración
Crear archivo .env:

env
FLASK_APP=app.py
FLASK_ENV=development
JWT_SECRET_KEY=tu_super_clave_secreta
Inicializar base de datos:

bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
🏃 Ejecución
bash
flask run

📡 Endpoints
🔓 Públicos
Método	Endpoint	Descripción	Body de Ejemplo
POST	/registro	Registrar nuevo usuario	{"nombre":"test","contraseña":"123"}
POST	/login	Iniciar sesión	{"nombre":"test","contraseña":"123"}

🔐 Protegidos (requieren token)
Método	Endpoint	Descripción	Header Requerido
GET	/protegido	Ruta de prueba protegida	Authorization: Bearer <token>

🧪 Ejemplos de Uso
Registro
bash
curl -X POST http://localhost:5000/registro \
  -H "Content-Type: application/json" \
  -d '{"nombre":"test","contraseña":"123"}'
Login
bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"nombre":"test","contraseña":"123"}'
Ruta protegida
bash
curl http://localhost:5000/protegido \
  -H "Authorization: Bearer <token>"

🛡️ Seguridad
Contraseñas almacenadas como hash bcrypt

Tokens JWT con expiración

Validación de datos de entrada

📄 Licencia
MIT

✉️ Contacto
Tu Nombre - @tu_twitter - tu@email.com

text

### Características adicionales que puedes incluir:
1. **Badges** al inicio (build status, coverage, etc.)
2. **Diagrama de flujo** de autenticación
3. **Ejemplos en Postman** con capturas
4. **Variables de entorno** requeridas
5. **Guía de contribución**