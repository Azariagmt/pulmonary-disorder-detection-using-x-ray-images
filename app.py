from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
import numpy as np # Fundamental package for linear algebra and multidimensional arrays
import tensorflow as tf # Deep Learning Tool
from tensorflow.keras.models import load_model
import os # OS module in Python provides a way of using operating system dependent functionality
import cv2 # Library for image processing
import shutil

MODEL_PATH = ''
def model_from_drive():
    global MODEL_PATH
    # https://drive.google.com/file/d/1-2cRvRkTnWNoGv6pNTAVBiC72-4BoVO0/view?usp=sharing
    # https://drive.google.com/file/d/18691v06KVU_TsFfN5WceJZ6sDS8tjYaG/view?usp=sharing
    # https://drive.google.com/file/d/16Tg8vU7IpB7Xg8hvrAEAsyz8OrjlEQvv/view?usp=sharing
    # from google_drive_downloader import GoogleDriveDownloader as gdd
    # gdd.download_file_from_google_drive(file_id='16Tg8vU7IpB7Xg8hvrAEAsyz8OrjlEQvv',
    #     dest_path='./model/binary-covid-model-6.h5',
    # )
    if (not os.path.isfile('binary-model.h5')):
        import gdown
        url = 'https://drive.google.com/uc?id=16Tg8vU7IpB7Xg8hvrAEAsyz8OrjlEQvv'
        output = 'binary-model.h5'
        gdown.download(url, output, quiet=False)
        MODEL_PATH = 'binary-model.h5'
    else: 
        print('file exists')
        MODEL_PATH = 'binary-model.h5'

def model_from_local():
    global MODEL_PATH
    MODEL_PATH = 'models/covidet.h5'
    
model_from_drive()
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
    print('predicted on Array :', img_array)
    prediction = model.predict(img_array)
    print('Prediction: \n', prediction, prediction[0])
    return prediction

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/binary', methods=['GET', 'POST'])
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
    os.environ.setdefault('Flask_SETTINGS_MODULE', 'helloworld.settings')
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True, port=port)