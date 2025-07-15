from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User  # Importamos el modelo y la base de datos

from forms import RegisterForm, LoginForm

# Creamos un Blueprint para agrupar las rutas relacionadas con autenticación
bp = Blueprint('auth', __name__)

# Ruta para el formulario de login
@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Buscar el usuario en la base de datos
        user = User.query.filter_by(username=form.username.data).first()

        if user and check_password_hash(user.password, form.password.data):
            # Si la contraseña es válida, iniciamos sesión
            login_user(user)
            flash("Has iniciado sesión correctamente", "success")
            return redirect(url_for("auth.user_dashboard"))  # Ruta protegida (a definir)

        flash("Nombre de usuario o contraseña incorrectos", "danger")

    return render_template("login.html", form=form)

# Ruta para el registro de nuevos usuarios
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))  # Evita que usuarios logueados vean esta página

    form = RegisterForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('El nombre de usuario ya existe.', 'danger')
            return redirect(url_for('auth.register'))

        hashed_password = generate_password_hash(form.password.data)

        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)

# Ruta protegida: solo accesible si el usuario ha iniciado sesión
@bp.route('/dashboard')
@login_required  # Requiere que el usuario esté autenticado
def user_dashboard():
    return render_template("dashboard.html", user=current_user)

# Ruta para cerrar sesión
@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Has cerrado sesión", "info")
    return redirect(url_for("index"))

# Ruta protegida solo para administradores
@bp.route('/admin')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        return redirect(url_for('auth.user_dashboard'))
    users = User.query.all()  # <-- Asegúrate de tener esta línea
    return render_template('admin.html', users=users)  # <-- Pasar los usuarios
