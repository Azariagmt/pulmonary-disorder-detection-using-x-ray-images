from flask import request
from werkzeug.utils import secure_filename
import os


file_path = ''
def get_image():
    global file_path
    f = request.files['file']
    print('f:\n\n  ',f)
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(
        basepath, '../upload/', secure_filename(f.filename))
    f.save(file_path)
    return file_path
