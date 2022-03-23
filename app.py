from enum import unique
import re
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FinKit.db'
db = SQLAlchemy(app)


class Accounts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    FirstName = db.Column(db.String(length=30), nullable=False)
    LastName = db.Column(db.String(length=30), nullable=False)
    Email = db.Column(db.String(length=50), nullable=False)
    Username = db.Column(db.String(length=30), nullable=False, unique=True)
    AccountType = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'Accounts {self.Username}'

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('regsiter.html')

@app.route('/stock')
def stock_page():
    return render_template('stockPage.html')
    
@app.route('/admin')
def admin_page():
    Accounts = Accounts.query.all()
    return render_template('accountInfo.html', Accounts=Accounts )