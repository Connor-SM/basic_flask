from app import app
from flask import render_template, url_for, redirect

@app.route('/')
@app.route('/index')
def index():
    name = 'Max'
    num = 3
    names = ['Connor', 'Chet', 'Todd', 'Tyler', 'Fiona', 'Tara']
    return render_template('index.html', name=name, num=num, names=names)

@app.route('/data')
def data_func():
    person = {
        'name': 'Max',
        'weight': 185,
        'height': 72,
        'eyes': 'Blue',
        'active': True
    }
    return render_template('data.html', person=person)

@app.route('/redirecting')
def my_redirect():
    return redirect(url_for('index'))
