from wtforms import Form, HiddenField
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.fields.html5 import EmailField

from .models import User


def codi_validator(form, field):
    if field.data == 'codi' or field.data == 'Codi':
        raise validators.ValidationError('El username codi no es permitido')

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('Solo los humanos pueden completar el registro ¬_¬')
class LoginForm(Form):
    username = StringField("Username", [
        validators.length(min=4, max=50, message="El username se encuentra fuera de rango")
    ])
    password = PasswordField("Password", [
        validators.Required(message='El password es requerido')
    ])

class RegisterForm(Form):
    honeypot = HiddenField('',[length_honeypot])


    username = StringField('Username',[
        validators.length(min=4, max=50),
        codi_validator
    ])
    email = EmailField('Correo electronico',[
        validators.length(min=6, max=100),
        validators.Required(message='El email es requerido'),
        validators.Email(message='Ingrese un email valido')
    ])
    password = PasswordField('Password',[
        validators.Required('El password es requerido'),
        validators.EqualTo('confirm_password', message='La contraseña no coincide')
    ])
    confirm_password = PasswordField('Confirm password')
    accept = BooleanField('Acepta terminos y condiciones',[
        validators.DataRequired()
    ])

    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError('El username ya se encuentra en uso')

    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError('El email ya se encuentra en uso')

class TaskForm(Form):
    title = StringField('Titulo', [
        validators.length(min=4, max=50, message='Titulo fuera de rango'),
        validators.DataRequired(message="El titulo es requerido")
    ])
    description = TextAreaField('Descripción', [
         validators.DataRequired(message='La descripción es requerida')    
    ], render_kw={'rows':5})