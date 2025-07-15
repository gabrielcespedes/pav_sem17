# Proyecto Flask con Autenticación de Usuarios

## Descripción

Este proyecto es una aplicación web en Flask que implementa un sistema de **autenticación y autorización de usuarios**, con roles diferenciados (`user` y `admin`), seguridad reforzada (CSRF, session signing, escape XSS) y una estructura modular para expandirla con nuevas funcionalidades.

---

## Tecnologías utilizadas

- **Python 3.13**
- **Flask 3.1.1**
- **Flask-Login**
- **Flask-WTF**
- **Flask SQLAlchemy**
- **Jinja2**
- **Bootstrap** (estilos y responsive)
- **SQLite** (base de datos local para prueba)
- **python-dotenv** (variables de entorno)

---

## Estructura del proyecto


```text
pav_sem17/
├── app.py                 # Configuración de la app y registro de Blueprints
├── auth.py                # Blueprint de autenticación: registro, login, logout, dashboards
├── models.py              # Modelos ORM: User (id, username, password, role)
├── forms.py               # Formularios de registro/login con validaciones y CSRF
├── requirements.txt       # Dependencias del proyecto
├── .env                   # Variables de entorno (no incluido, agregar manualmente)
├── /templates/            # Templates con Jinja2
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   └── dashboard_admin.html
└── static/
    └── img/
        └── security.jpg   # Imagen decorativa en la página de inicio
```
---

## Seguridad implementada

| Vulnerabilidad     | Protección                                                                 |
|--------------------|----------------------------------------------------------------------------|
| CSRF               | Tokens automáticos con Flask-WTF                                           |
| XSS                | Escape automático de Jinja2                                                |
| SQL Injection      | ORM SQLAlchemy                                                             |
| Firmado de sesiones| `SECRET_KEY` criptográficamente firma cookies y formularios               |
| Autorización       | Rutas protegidas con `@login_required` y validación de roles de usuario    |

La clave secreta de la app (`SECRET_KEY`) se almacena en el archivo `.env`. 

---

## Funcionalidades

- **Página de inicio** (`/`): bienvenida con imagen y navbar.
- **Registro de usuario** (`/register`): formulario con validación.
- **Inicio de sesión** (`/login`) y **logout** (`/logout`).
- **Dashboard de usuario** (`/dashboard`): solo accesible si estás autenticado como `user`.
- **Dashboard de administrador** (`/admin-dashboard`): solo accesible si tu rol es `admin`.
- Enlaces del navbar adaptados al estado de autenticación y rol.

---

## Instalación y ejecución

1. **Clona el repositorio**

```bash
git clone https://github.com/gabrielcespedes/pav_sem17.git
cd pav_sem17
```

2. **Crea y activa el entorno virtual**
```bash
python3 -m venv venv
source venv/bin/activate  # o venv\Scripts\activate (en Windows)
```
3. **Instala dependencias**
```bash
pip install -r requirements.txt
```

4. **Configura variables de entorno**
```init
SECRET_KEY=<tu_clave_generada_con_secrets.token_hex(32)>
```

5. **Ejecuta la aplicación**
```bash
python app.py
```

### **Uso**
- Regístrate con una cuenta personalizada (rol ```user``` por defecto)
- Ingresa con tu usuario
- Para cambiar a rol ```admin```, ejecuta en consola

```python
from models import db, User
user = User.query.filter_by(username = 'nombre_de_usuario').first()
user.role = "admin"
db.session.commit()
```
### **Notas**
- Actualmente, las rutas del BLueprint de autenticación **no usan prefijo** (```/login```, ```/register```, etc.)-
- Si desea agrupar, por ejemplo, bajo ```/auth/``` modifique la línea en ```app.py```_

```python
app.register_blueprint(auth.bp, url_prefix = '/auth')
```

Y ajuste los ```url_for()``` en los templates correspondientes.