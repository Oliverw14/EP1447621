from FinKit import db
from FinKit import bcrypt
from FinKit import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    Username = db.Column(db.String(length=30), nullable=False, unique=True)
    FirstName = db.Column(db.String(length=30), nullable=False)
    LastName = db.Column(db.String(length=30), nullable=False)
    Email = db.Column(db.String(length=50), nullable=False, unique=True)
    Password_hash = db.Column(db.String(60), nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.Password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.Password_hash, attempted_password)
        

class Accounts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    FirstName = db.Column(db.String(length=30), nullable=False)
    LastName = db.Column(db.String(length=30), nullable=False)
    Email = db.Column(db.String(length=50), nullable=False)
    Username = db.Column(db.String(length=30), nullable=False, unique=True)
    AccountType = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'Accounts {self.Username}'