from flask import Flask, render_template, request, redirect
import pandas as pd
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('product.db')

# def extract_data(data_df):
#     data_key = [row[1][0] for row in data_df.iterrows()]
#     data_col = data_df.columns.to_list()[1:]
#     data_body = []

#     for row in data_df.iterrows():
#         data_body.append(dict(zip(data_col, row[1][1:])))

#     complete_data = dict(zip(data_key, data_body))
#     return complete_data

def update_sql(type, conn, task, id):
    if type == 'product':
        sql = f''' UPDATE product
                    SET product_name = ? ,
                        product_price = ? ,
                        product_cat = ?,
                        product_review = ?,
                        color = ?,
                        material = ?,
                        offer = ?,
                        product_detail = ?
                    WHERE product_id = {id}'''
    else:
        return
    
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

product_df = pd.read_csv(r'C:\Users\HP\Documents\GitHub\midTerm.github.io\src\productData.csv', encoding= 'utf8')
rows = [tuple(row[1].to_list()) for row in product_df.iterrows()]

for row in rows:
    update_sql('product', conn, row[1:], row[0])
# Use executemany() to insert multiple records at a time

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