from flask import Flask, render_template
from random import *
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    tr = True
    random_number = randint(1, 10)
    now = datetime.datetime.now()
    year = now.year
    return render_template('index.html', num=random_number, year=year)


@app.route('/guess/<name>')
def guess(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    text = response.json()
    age = text["age"]
    name = text["name"]
    return render_template('index1.html', name=name, age=age)


app.run(debug=True)
