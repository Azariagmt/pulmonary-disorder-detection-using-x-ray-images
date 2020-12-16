from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import numpy as np # Fundamental package for linear algebra and multidimensional arrays
from keras.models import load_model
import tensorflow as tf # Deep Learning Tool
import os # OS module in Python provides a way of using operating system dependent functionality
import cv2 # Library for image processing
# from sklearn.metrics import f1_score

MODEL_PATH = 'models/covidet.h5'
# Load your trained model
model = load_model(MODEL_PATH)

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
    # img_array = np.array(img_array)
    prediction = model.predict(img_array)
    print('Prediction: \n', prediction, prediction[0])
    return prediction

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        print('f:\n\n  ',f)
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'upload/', secure_filename(f.filename))
        f.save(file_path)
        prediction = model_predict(file_path, model)
        if (prediction[0] >=0.5):
            return '+'
        elif (prediction[0]<0.5):
            return '-'
        else:
            return 'None'

if __name__ == '__main__':
    os.environ.setdefault('FLASK_SETTINGS_MODULE', 'web_project.settings')
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0',debug=True)

