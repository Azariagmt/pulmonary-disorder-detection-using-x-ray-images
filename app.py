from copy import Error
from sal import saliency
from flask import Flask, render_template, request, Response, copy_current_request_context
from werkzeug.exceptions import Forbidden, HTTPException, NotFound, RequestTimeout, Unauthorized
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
import numpy as np
import pandas as pd
from modules import model_handler, predict, image_processing
import json
# from flask import CORS
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/binary', methods=['GET', 'POST'])
def predict_binary():
    """Function predicting binary model

    Returns:
        result (string): + or - depending on probability someone has covid or not
    """
    if request.method == 'POST':
        binary_model = model_handler.get_model("binary")
        prediction = predict.model_predict(
            image_processing.get_image(), binary_model)
        if (prediction[0] >= 0.5):
            return '+'
        elif (prediction[0] < 0.5):
            return '-'
    return None

CLASS_NAMES = ['Covid 19', 'Bacterial Pneumonia',
               'Viral Pneumonia', 'Tuberculosis', 'Normal']

@app.route('/multiclass', methods=['GET', 'POST'])
def predict_multiclass():
    """function predicting multiclass model

    Returns:
        result: the classname of the highest predicted index using argmax
    """
    global CLASS_NAMES
    if request.method == 'POST':
        multiclass_model = model_handler.get_model("multiclass")
        multiclass_prediction = predict.model_predict(
            image_processing.get_image(), multiclass_model)
        
        predicted_class_indices = np.argmax(multiclass_prediction, axis=1)
        result = CLASS_NAMES[predicted_class_indices[0]]
        return result
    return None



@app.route("/api/multiclass", methods=['GET', 'POST'])
def multiclass_api():
    """API for predicting multiclass model
    Recieves POST request with URL containing json content in body
    Example:
        {
        "url":"https://someimg.png"
        }
    Returns:
        result: Array containing prediction value for each class
    """
    global CLASS_NAMES
    if request.method == "POST":
        img_path = request.get_json()['url']
        print("IMAGE PATH=============", img_path)
        multiclass_model = model_handler.get_model("multiclass")
        multiclass_prediction = predict.model_predict(
            img_path, multiclass_model)
        print(multiclass_prediction)
        # @copy_current_request_context
        import datetime

        datetime_object = datetime.datetime.now()
        def saliency_generation(multiclass_model):
            import sal
            sal.saliency(img_path=img_path, multiclass_model=multiclass_model, name=datetime_object)
        
        saliency_generation(multiclass_model=multiclass_model)
        # import threading
        # threading.Thread(target=saliency_generation).start()

        return {
            "prediction": pd.Series(multiclass_prediction[0]).to_json(orient='values'),
            "saliency": f"/static/img/saliency/{datetime_object}.png"
            }
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
