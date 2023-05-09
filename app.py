from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product/<id>')
def product(id):
    return render_template('product.html', id= id)

app.run(debug= True)