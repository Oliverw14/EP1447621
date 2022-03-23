import imp
import re
from FinKit import app
from flask import render_template, redirect, url_for
from FinKit.models import Accounts, User
from FinKit.forms import RegisterForm
from FinKit import db

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(Username=form.username.data, 
                              FirstName=form.firstname.data,
                              LastName=form.lastname.data,
                              Email=form.email_address.data,
                              Password_hash=form.password_1.data )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('stock_page'))

    if form.errors != {}:#if there are no errors from validators
        for err_msg in form.errors.values():
            print(f'There was an error in creating a user: {err_msg}')

    return render_template('register.html', form=form)

@app.route('/stock')
def stock_page():
    return render_template('stockPage.html')
    
@app.route('/admin')
def admin_page():
    users = User.query.all()
    return render_template('accountInfo.html', Users=users )