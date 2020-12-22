from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from werkzeug.exceptions import Forbidden, HTTPException, NotFound, RequestTimeout, Unauthorized
import numpy as np # Fundamental package for linear algebra and multidimensional arrays
import tensorflow as tf
from tensorflow.keras.models import load_model
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
    if (not os.path.exists('{}/../binary-model.h5'.format(BASE_DIR))):
        url = 'https://drive.google.com/uc?id=1Zs3xrGGKIAbq_3uDG5X2Sj6H2sUsPmB0'
        output = 'binary-model.h5'
        gdown.download(url, output, quiet=False)
        BINARY_MODEL_PATH = '{}/../binary-model.h5'.format(BASE_DIR)
        print('BINARY MODEL SUCCESS'
)
    else:
        print('Binar model exists=========================================')
        BINARY_MODEL_PATH = '{}/../binary-model.h5'.format(BASE_DIR)
    # Load your trained model

    BINARY_MODEL = load_model(BINARY_MODEL_PATH)
    return BINARY_MODEL


def load_multiclass_model():
    global MULTICLASS_MODEL_PATH
    global MULTICLASS_MODEL
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    print('BASE DIRECTORY : ',BASE_DIR)
    if (not os.path.exists('{}/../multiclass-model.h5'.format(BASE_DIR))):
        url = 'https://drive.google.com/uc?id=1LUJK_QVdWuZzJeOdsfg5R3F_OXLKt3rt'
        output = 'multiclass-model.h5'
        gdown.download(url, output, quiet=False)
        MULTICLASS_MODEL_PATH = '{}/../multiclass-model.h5'.format(BASE_DIR)
        print('MULTICLASS MODEL SUCCESS')
    else:
        print('Multiclass model exist=========================================')
        MULTICLASS_MODEL_PATH = '{}/../multiclass-model.h5'.format(BASE_DIR)
    # Load your trained model

    MULTICLASS_MODEL = load_model(MULTICLASS_MODEL_PATH)
    return MULTICLASS_MODEL