from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FinKit.db'
app.config['SECRET_KEY'] = 'b86deabcf9bb356c549532d6'
db = SQLAlchemy(app)

from FinKit import routes