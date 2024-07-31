from flask import Flask
# pip install -U flask-cors
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/hardware")
@cross_origin()
def hardware():
    return {
        'projectId': '3',
        'capacity': '100',
        'availability': '100',
        'request': '0'
    }