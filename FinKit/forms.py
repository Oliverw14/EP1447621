from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label='Username:', validators = [Length(min=2, max=30), DataRequired()])
    firstname = StringField(label='First Name:', validators=[Length(min=2, max=30), DataRequired()])
    lastname = StringField(label='Last Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password_1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password_2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password_1'), DataRequired()])
    submit = SubmitField(label='Create Account')