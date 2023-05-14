from flask import Flask, render_template, request, redirect
import pandas as pd
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('product.db')
cur = conn.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    test = 'test'
    review = request.form.get('review_select')
    return render_template('index.html', review= review, test= test)

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/filterData')
def filterData():
    test = request.form['test-text']
    return render_template('fetchtestpage.html', test= test)

@app.route('/fetchtestpage', methods= ['GET', 'POST'])
def fetchtestpage():
    return render_template('fetchtestpage.html')

@app.route('/fetchtest', methods= ['GET', 'POST'])
def fetchtest():
    return {'some text': 'it was a success!'}

app.run(debug= True)