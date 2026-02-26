from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/product')
def product():
    return render_template('product.html')
