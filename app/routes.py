from flask import render_template, request
from . import app

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/partners')
def parners():
    return render_template('partners.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/products')
def products():
    return render_template('products.html')