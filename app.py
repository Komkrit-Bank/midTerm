from flask import Flask, render_template, request, redirect
import pandas as pd
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('product.db')
cur = conn.cursor()

# def extract_data(data_df):
#     data_cat = [row[1][3] for row in data_df.iterrows()]
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
                        product_detail = ?,
                        product_img = ?
                    WHERE product_id = {id}'''
    else:
        return
    
    cur.execute(sql, task)
    conn.commit()
    
def filter_data(column, con):
    cur.execute(f'SELECT * FROM product WHERE {column} = ?', (con,))
    data = cur.fetchall()
    return data

product_df = pd.read_csv(r'src\productData.csv', encoding= 'utf8')
rows = [tuple(row[1].to_list()) for row in product_df.iterrows()]
product_col = product_df.columns.to_list()

for row in rows:
    update_sql('product', conn, row[1:], row[0])
# Use executemany() to insert multiple records at a time

@app.route('/', methods=['GET', 'POST'])
def index():
    products = rows
    category = 'console'
    review = request.form.get('review_select')
    return render_template('index.html', review= review, products= products, category= category)

@app.route('/product/<int:id>')
def product(id):
    pro_detail = product_df[product_df['product_id'] == id].iloc[0, :][1:].to_dict()
    print(pro_detail)
    return render_template('product.html', pro_detail= pro_detail)

@app.route('/information', methods= ['GET', 'POST'])
def information():
    return render_template('information.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

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

if __name__ == '__main__':
    app.run(debug= True)