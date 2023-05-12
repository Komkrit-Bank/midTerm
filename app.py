from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    test = 'test'
    review = request.form.get('review_select')
    return render_template('index.html', review= review, test= test)

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/fetchtestpage', methods= ['GET', 'POST'])
def fetchtestpage():
    return render_template('fetchtestpage.html')

@app.route('/fetchtest', methods= ['GET', 'POST'])
def fetchtest():
    return {'some text': 'it was a success!'}

app.run(debug= True)