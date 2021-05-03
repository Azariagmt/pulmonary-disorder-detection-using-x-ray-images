from flask import Flask, render_template, request
from werkzeug.exceptions import Forbidden, HTTPException, NotFound, RequestTimeout, Unauthorized
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
import numpy as np 
from modules import load_models, predict, image_processing

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/binary', methods=['GET', 'POST'])
def predict_binary():
    if request.method == 'POST':
        load_models.load_binary_model()
        prediction = predict.model_predict(image_processing.get_image(),load_models.BINARY_MODEL)
        if (prediction[0] >=0.5):
            return '+'
        elif (prediction[0]<0.5):
            return '-'
    return None 

CLASS_NAMES = ['Covid 19', 'Bacterial Pneumonia', 'Viral Pneumonia','Tuberculosis', 'Normal']
@app.route('/multiclass', methods=['GET', 'POST'])
def predict_multiclass():
    global CLASS_NAMES
    if request.method == 'POST':
        load_models.load_multiclass_model()
        multiclass_prediction = predict.model_predict(image_processing.get_image(), load_models.MULTICLASS_MODEL)
        predicted_class_indices  = np.argmax(multiclass_prediction,axis=1)
        result = CLASS_NAMES[predicted_class_indices[0]]
        return result
    return None 

@app.errorhandler(NotFound)
def page_not_found_handler(e: HTTPException):
    return '<h1>404.html</h1>', 404

@app.errorhandler(Unauthorized)
def unauthorized_handler(e: HTTPException):
    return '<h1>401.html</h1>', 401

@app.errorhandler(Forbidden)
def forbidden_handler(e: HTTPException):
    return '<h1>403.html</h1>', 403

@app.errorhandler(RequestTimeout)
def request_timeout_handler(e: HTTPException):
    return '<h1>408.html</h1>', 408

if __name__ == '__main__':
    os.environ.setdefault('Flask_SETTINGS_MODULE', 'helloworld.settings')
    app.run(debug=True)