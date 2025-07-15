"""
from flask import redirect, url_for, flash
from flask_login import current_user
from functools import wraps

# Decorador para restringir el acceso a administradores
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("Debes iniciar sesión primero.", "warning")
            return redirect(url_for("auth.login"))
        if current_user.role != "admin":
            flash("No tienes permisos para acceder a esta página.", "danger")
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return decorated_function
"""