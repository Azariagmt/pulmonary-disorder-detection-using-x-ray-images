import os
import tensorflow as tf # Deep Learning Tool
from tensorflow.keras.models import load_model
from keras import backend as K
import os # OS module in Python provides a way of using operating system dependent functionality
import shutil
import gdown

BINARY_MODEL_PATH = ''
MULTICLASS_MODEL_PATH = ''
BINARY_MODEL = ''
MULTICLASS_MODEL = ''

def load_binary_model():
    global BINARY_MODEL_PATH
    global BINARY_MODEL
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    print('BASE DIRECTORY : ',BASE_DIR)
    if(os.path.exists('{}/../models/binary-model.h5'.format(BASE_DIR))):
        BINARY_MODEL_PATH = '{}/../models/binary-model.h5'.format(BASE_DIR)
    else:
        url = 'https://drive.google.com/uc?id=1Zs3xrGGKIAbq_3uDG5X2Sj6H2sUsPmB0'
        output = '../models/binary-model.h5'
        gdown.download(url, output, quiet=False)
        BINARY_MODEL_PATH = '{}/../models/binary-model.h5'.format(BASE_DIR)
        print('BINARY MODEL DOWNLOADED')

    # Load your trained model

    BINARY_MODEL = load_model(BINARY_MODEL_PATH)
    return BINARY_MODEL

def load_multiclass_model():
    global MULTICLASS_MODEL_PATH
    global MULTICLASS_MODEL
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    print('BASE DIRECTORY : ',BASE_DIR)
    if (os.path.exists('{}/../models/multiclass-model.h5'.format(BASE_DIR))):
        MULTICLASS_MODEL_PATH = '{}/../models/multiclass-model.h5'.format(BASE_DIR) 
    else:
        # if app is not being used via docker
        url = 'https://drive.google.com/uc?id=1LUJK_QVdWuZzJeOdsfg5R3F_OXLKt3rt'
        output = '../models/multiclass-model.h5'
        gdown.download(url, output, quiet=False)
        MULTICLASS_MODEL_PATH = '{}/../models/multiclass-model.h5'.format(BASE_DIR)
        print('MULTICLASS MODEL DOWNLOADED')

    # Load your trained model

    MULTICLASS_MODEL = load_model(MULTICLASS_MODEL_PATH)
    return MULTICLASS_MODEL
