from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from werkzeug.exceptions import Forbidden, HTTPException, NotFound, RequestTimeout, Unauthorized
import numpy as np # Fundamental package for linear algebra and multidimensional arrays
import tensorflow as tf
from tensorflow.keras.models import load_model
import os # OS module in Python provides a way of using operating system dependent functionality
import cv2 # Library for image processing
import shutil
import gdown
from modules import load_models


# def model_from_local():
#     global BINARY_MODEL_PATH
#     BINARY_MODEL_PATH = 'models/bin.h5'

app = Flask(__name__)

def model_predict(img_path, model):
    data = [] # initialize an empty numpy array
    image_size = 100 # image size taken is 100 here. one can take other size too
    img_array = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) # converting the image to gray scale
    print('Image array shape: \n\n', img_array.shape)
    img_array = cv2.resize(img_array, (image_size,image_size)) # resizing the image array
    print('Image array shape: \n\n', img_array.shape)
    img_array = np.stack((img_array,)*3, axis=-1)
    img_array = np.expand_dims(img_array, axis=0)
    print('Image array shape: ', img_array.shape)
    # img_array = np.array(img_array)
    print('predicted on Array :', img_array)
    prediction = model.predict(img_array)
    print('Prediction: \n', prediction, prediction[0])
    return prediction

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/binary', methods=['GET', 'POST'])
def uploadb():
    if request.method == 'POST':
        f = request.files['file']
        print('f:\n\n  ',f)
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'upload/', secure_filename(f.filename))
        f.save(file_path)
        load_models.BINARY_MODEL = load_models.load_binary_model()
        print('BINARY MODEL LOADED')
        prediction = model_predict(file_path, load_models.BINARY_MODEL)
        print('BINARY PREDICTION',prediction)
        if (prediction[0] >=0.5):
            return '+'
        elif (prediction[0]<0.5):
            return '-'
    return None 

CLASS_NAMES = ['Covid 19', 'Pneumonia', 'Tuberculosis']
@app.route('/predict/multiclass', methods=['GET', 'POST'])
def uploadm():
    global CLASS_NAMES
    if request.method == 'POST':
        f = request.files['file']
        print('f:\n\n  ',f)
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'upload/', secure_filename(f.filename))
        f.save(file_path)
        load_models.MULTICLASS_MODEL = load_models.load_multiclass_model()
        multiclass_prediction = model_predict(file_path, load_models.MULTICLASS_MODEL)
        predicted_class_indices  = np.argmax(multiclass_prediction,axis=1)
        res = CLASS_NAMES[predicted_class_indices[0]]
        return res
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