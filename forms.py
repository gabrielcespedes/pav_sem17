# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, DataRequired

# Formulario de registro
class RegisterForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[InputRequired(), Length(min=4, max=150)])
    password = PasswordField('Contraseña', validators=[InputRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar contraseña', validators=[
        InputRequired(),
        EqualTo('password', message='Las contraseñas deben coincidir')
    ])
    submit = SubmitField('Registrarse')

# Formulario de login
class LoginForm(FlaskForm):
    username = StringField("Nombre de usuario", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Iniciar sesión")