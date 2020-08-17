from flask import Flask
from main import *

app = Flask(__name__)
@app.route('/search/<query>')
def home(query):
    return createOutput(query)
if __name__ == '__main__':
    app.run(debug=True)