from flask import *


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/blog', methods = ['GET', 'POST'])
def blog():
    return render_template('blog.html')

app.run(host='0.0.0.0', port=5000, debug=True)