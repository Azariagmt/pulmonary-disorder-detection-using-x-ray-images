import os
import numpy as np
import cv2
import urllib
import numpy as np
import cv2

from urllib.request import urlopen
def url_to_image(url, readFlag=cv2.IMREAD_COLOR):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urlopen(url, timeout=100)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, readFlag)

    # return the image
    return image



def preprocess_image(img_path):
    data = [] # initialize an empty numpy array
    image_size = 100 # image size taken is 100 here. one can take other size too

    img_array = url_to_image(img_path)

    img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    print(img_array.shape)
    img_array = cv2.resize(img_array, (image_size,image_size)) # resizing the image array
    # should be (1,100,100,3)
    img_array = np.stack((img_array,)*3, axis=-1)
    img_array = np.expand_dims(img_array, axis=0)
    print('Image array shape: ', img_array.shape)
    # img_array = np.array(img_array)
    print('predicted on Array :', img_array)
    return img_array

def model_predict(img_path, model):
    img_array = preprocess_image(img_path)
    prediction = model.predict(img_array)
    print('Prediction: \n', prediction, prediction[0])
    return prediction