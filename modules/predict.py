import os
import numpy as np
import cv2


def preprocess_image(img_path):
    data = [] # initialize an empty numpy array
    image_size = 100 # image size taken is 100 here. one can take other size too
    img_array = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) # converting the image to gray scale
    img_array = cv2.resize(img_array, (image_size,image_size)) # resizing the image array
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