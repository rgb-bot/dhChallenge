from flask import Flask
from parse import *

app = Flask(__name__)
@app.route('/search/<query>')
def home(query):
    return parse(query)
if __name__ == '__main__':
    app.run(debug=True)