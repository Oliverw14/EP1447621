from FinKit import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from FinKit.models import Accounts, User
from FinKit.forms import RegisterForm, LoginForm
from FinKit import db
from flask_login import login_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(Username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f"Success! You are logged in as: {attempted_user.Username}", category='success')
            return redirect(url_for('stock_page'))
        else:
            flash("Username or Password are incorrect! Please try again", category='danger')

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(Username=form.username.data, 
                              FirstName=form.firstname.data,
                              LastName=form.lastname.data,
                              Email=form.email_address.data,
                              password=form.password_1.data )
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Success! Account created successfully. You are logged in as: {user_to_create.Username}", category='success')
        return redirect(url_for('stock_page'))

    if form.errors != {}:#if there are no errors from validators
        for err_msg in form.errors.values():
            flash(f'There was an error in creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/stock')
@login_required
def stock_page():
    return render_template('stockPage.html')
    
@app.route('/admin')
def admin_page():
    users = User.query.all()
    return render_template('accountInfo.html', Users=users )

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for('home_page'))