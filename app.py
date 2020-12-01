from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import pandas as pd # Data analysis and manipultion tool
import numpy as np # Fundamental package for linear algebra and multidimensional arrays
import matplotlib.pyplot as plt
# import tensorflow as tf # Deep Learning Tool
# import os # OS module in Python provides a way of using operating system dependent functionality
# import cv2 # Library for image processing
# from sklearn.model_selection import train_test_split # For splitting the data into train and validation set
# from sklearn.metrics import f1_score

app = Flask(__name__)

def model_predict(img_path, model):
    data = [] # initialize an empty numpy array
    image_size = 100 # image size taken is 100 here. one can take other size too
    img_array = cv2.imread(train_data['filepaths'][i], cv2.IMREAD_GRAYSCALE) # converting the image to gray scale
    new_img_array = cv2.resize(img_array, (image_size, image_size)) # resizing the image array
    data.append([new_img_array, train_data['label'][i]])
    pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        print('f:  ',f)
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads/', secure_filename(f.filename))
        f.save(file_path)
        preds = model_predict(file_path, model)
        return 'None'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0',debug=True, port=port)

