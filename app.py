# app.py
from flask import Flask, render_template
from models import Product

app = Flask(__name__)

@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)
