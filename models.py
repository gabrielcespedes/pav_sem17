from flask_sqlalchemy import SQLAlchemy  # ORM para manejar la base de datos
from flask_login import UserMixin  # Clase base para usuarios autenticados

# Instanciamos SQLAlchemy (esto se inicializará en app.py)
db = SQLAlchemy()

# Creamos la clase User como modelo para la tabla 'users'
class User(db.Model, UserMixin):
    __tablename__ = 'users'  # Nombre explícito de la tabla

    id = db.Column(db.Integer, primary_key=True)  # ID único del usuario
    username = db.Column(db.String(150), unique=True, nullable=False)  # Nombre de usuario
    password = db.Column(db.String(200), nullable=False)  # Contraseña en formato hash
    role = db.Column(db.String(50), nullable=False, default='user')  # Rol del usuario: 'admin', 'user', etc.

    def __repr__(self):
        # Representación útil para depurar
        return f'<User {self.username} ({self.role})>'
