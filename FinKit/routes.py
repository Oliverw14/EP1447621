from FinKit import app
from flask import render_template, redirect, request, url_for, flash, get_flashed_messages
from FinKit.models import Accounts, User
from FinKit.forms import RegisterForm, LoginForm, UserUpdateForm
from FinKit import db
from flask_login import login_user, logout_user, login_required
import pandas as pd
import json
import plotly
import plotly.express as px

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
    df = pd.read_csv('FinKit\data\yield_curve.csv')   
    df2 = pd.read_csv('FinKit\data\yield_distance.csv')
    df3 = pd.read_csv('FinKit\data\HSI_sma.csv', usecols=["date", "close_gt_sma50"])
    sdf3 = df3.sort_values(by='date', ascending=True)
    df4 = pd.read_csv('FinKit\data\HSI_sma.csv', usecols=["date", "close_gt_sma200"])
    sdf4 = df4.sort_values(by='date', ascending=True)
    fig = px.line(df, x='period', y='rate', title='Bond Yield Curve')
    fig2 = px.line(df2, x='Date', y='difference', title='Bond Yield Distance')
    fig3 = px.line(sdf3, x='date', y='close_gt_sma50', title='No of stocks > SMA50')
    fig3.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ]) 
        )
    )   
    fig4 = px.line(sdf4, x='date', y='close_gt_sma200', title='No of stocks > SMA200')
    fig4.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ]) 
        )
    )      
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder) 
    graphJSON3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)  
    graphJSON4 = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)   
    return render_template('stockPage.html', graphJSON1=graphJSON1, graphJSON2=graphJSON2,graphJSON3=graphJSON3,graphJSON4=graphJSON4)

    
@app.route('/admin')
def admin_page():
    users = User.query.all()
    return render_template('adminPage.html', Users=users )

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for('home_page'))

@app.route('/account/<int:id>', methods=['GET', 'POST'])
@login_required
def account_page(id):
    form = UserUpdateForm()
    show_user = User.query.filter_by(id=id).first()
    if form.validate_on_submit():
        show_user.Username = form.username.data
        show_user.FirstName = form.firstname.data
        show_user.LastName = form.lastname.data
        show_user.Email = form.email_address.data
        
        db.session.commit()
        flash(f'Details for {show_user.Username} updated', category='info')
    
    if form.errors != {}:#if there are no errors from validators
        for err_msg in form.errors.values():
            flash(f'There was an error in creating a user: {err_msg}', category='danger')
        
    
    return render_template('account.html', form=form, user=show_user, id=id)