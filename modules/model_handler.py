import os
import tensorflow as tf  # Deep Learning Tool
from tensorflow.keras.models import load_model
from keras import backend as K
import os  # OS module in Python provides a way of using operating system dependent functionality
import shutil
import gdown


class BinaryModelLoader:
    base_dir = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):
        if(not os.path.exists('{}/../models/binary-model.h5'.format(self.base_dir))):
            url = 'https://drive.google.com/uc?id=1Zs3xrGGKIAbq_3uDG5X2Sj6H2sUsPmB0'
            output = '{}/../models/binary-model.h5'.format(self.base_dir)
            gdown.download(url, output, quiet=False)
        self.path = '{}/../models/binary-model.h5'.format(
            BinaryModelLoader.base_dir)
        self.model = load_model(self.path)

    @property
    def fetched_model(self):
        return self.model


class MulticlassModelLoader:
    base_dir = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):
        if(not os.path.exists('{}/../models/multiclass-model.h5'.format(self.base_dir))):
            url = 'https://drive.google.com/uc?id=1LUJK_QVdWuZzJeOdsfg5R3F_OXLKt3rt'
            output = '{}/../models/multiclass-model.h5'.format(self.base_dir)
            gdown.download(url, output, quiet=False)
        self.path = '{}/../models/multiclass-model.h5'.format(
            MulticlassModelLoader.base_dir)
        self.model = load_model(self.path)

    @property
    def fetched_model(self):
        return self.model

def model_loading_factory(model_type):
    if model_type == "binary":
        loader = BinaryModelLoader()
    elif model_type == "multiclass":
        loader = MulticlassModelLoader()
    else:
        raise ValueError('Cannot get loader {}'.format(model_type))
    # return model from loader object
    return loader.fetched_model


#wrapper for model_loading_factory
def get_model(model_type):
    factory_obj = None
    try:
        factory_obj = model_loading_factory(model_type)
    except ValueError as e:
        print(e)
    return factory_obj


# to fetch models for docker image
if __name__ == "main":
    get_model("binary")
    get_model("multiclass")
