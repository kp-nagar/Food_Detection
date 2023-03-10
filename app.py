from flask import Flask, request, jsonify, render_template
from util import predict_class
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('app.html')


@app.route('/api/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']
    return jsonify(predict_class(image_data))
