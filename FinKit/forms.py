from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from FinKit.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(Username=username_to_check.data).first()
        if user:
            raise ValidationError('Username is taken! Please try a different username')

    def validate_email_address(self, email_to_check):
        email = User.query.filter_by(Email=email_to_check.data).first()
        if email:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='Username:', validators = [Length(min=2, max=30), DataRequired()])
    firstname = StringField(label='First Name:', validators=[Length(min=2, max=30), DataRequired()])
    lastname = StringField(label='Last Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password_1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password_2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password_1'), DataRequired()])
    submit = SubmitField(label='Create Account')