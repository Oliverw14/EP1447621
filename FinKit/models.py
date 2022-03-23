from FinKit import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Username = db.Column(db.String(length=30), nullable=False, unique=True)
    FirstName = db.Column(db.String(length=30), nullable=False)
    LastName = db.Column(db.String(length=30), nullable=False)
    Email = db.Column(db.String(length=50), nullable=False, unique=True)
    Password_hash = db.Column(db.String(60), nullable=False)


class Accounts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    FirstName = db.Column(db.String(length=30), nullable=False)
    LastName = db.Column(db.String(length=30), nullable=False)
    Email = db.Column(db.String(length=50), nullable=False)
    Username = db.Column(db.String(length=30), nullable=False, unique=True)
    AccountType = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'Accounts {self.Username}'