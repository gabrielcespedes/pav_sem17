import os  # Para manejar variables de entorno
from dotenv import load_dotenv  # Para cargar el archivo .env

from flask import Flask, render_template
from flask_login import LoginManager

from models import db

# Importar el modelo de usuario para login
from models import User

# Importar las rutas de autenticación
import auth

# Cargar variables de entorno desde .env
load_dotenv()

# Crear instancia de Flask
app = Flask(__name__)

# Configuraciones de la aplicación
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")  # Clave secreta para sesiones y CSRF
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"  # Base de datos SQLite
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Desactivar notificaciones innecesarias

# Inicializar la base de datos
db.init_app(app)

# Crear la base de datos si no existe (compatible con Flask 3.1.1)
with app.app_context():
    db.create_all()

# Configurar el sistema de login
login_manager = LoginManager()
login_manager.login_view = 'login'  # Redirigir a esta vista si el usuario no ha iniciado sesión
login_manager.init_app(app)

# Función requerida por Flask-Login para cargar el usuario actual
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Registrar las rutas definidas en auth.py
app.register_blueprint(auth.bp)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')  # Página base, puede cambiarse según las plantillas

# Ejecutar la aplicación (solo si se ejecuta directamente este archivo)
if __name__ == '__main__':
    app.run(debug=True)
