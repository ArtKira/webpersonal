from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField, RadioField, SelectField
from wtforms.validators import DataRequired, Email

################FORMULARIOS DE WTFORMS########################
class loginForm(FlaskForm):
    email=EmailField('Username', validators=[DataRequired(), Email()])#validamos los datos 
    password=PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Ingresar')

class RegisterForm(FlaskForm):
    name=StringField('Nombre')
    last_name=StringField('Apellido')
    email=EmailField('Correo')
    password=PasswordField('Contraseña')
    phone=IntegerField('Telefono')
    is_married=RadioField('Estado Civil', choices=[('True', 'casado'), ('False', 'soltero' )])
    gander=SelectField('Genero', choices=[('male', 'Masculino'), ('famale', 'Femenino' ), ('other', 'otro')])
    submit=SubmitField('Registrar')
