from keras.backend import dtype
from modules import model_handler
from modules.predict import preprocess_image

def saliency(img_path, multiclass_model, name):

    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import scipy.ndimage as ndimage
    from tensorflow.keras.preprocessing.image import load_img
    from tensorflow.keras.applications.densenet import preprocess_input
    import numpy as np

    # Preparing input data for VGG16
    # X = preprocess_input(images)
    # X = 'https://firebasestorage.googleapis.com/v0/b/intelrad-a680a.appspot.com/o/images%2Fxrayyyy.jpg?alt=media&token=63a8460f-5c79-422c-91d6-c5a2704d2383'
    X = img_path
    X = preprocess_image(X)
    # Rendering
    import matplotlib.pyplot as plt
    
    from tf_keras_vis.scorecam import Scorecam
    from matplotlib import cm
    from tf_keras_vis.gradcam import Gradcam
    from tf_keras_vis.utils.model_modifiers import ReplaceToLinear

    replace2linear = ReplaceToLinear()

    # Create Gradcam object
    gradcam = Gradcam(multiclass_model,
                    model_modifier=replace2linear,
                    clone=True)
    # Instead of using CategoricalScore object,

    from tf_keras_vis.utils.scores import CategoricalScore

    # 1 is the imagenet index corresponding to Goldfish, 294 to Bear and 413 to Assault Rifle.
    score = CategoricalScore(4)
    from tensorflow.keras import backend as K
    from tf_keras_vis.saliency import Saliency
    # from tf_keras_vis.utils import normalize

    # Create Saliency object.
    saliency = Saliency(multiclass_model,
                        model_modifier=replace2linear,
                        clone=True)

    # Generate saliency map
    X = X.tolist()
    X = np.asarray(X, dtype=np.float)
    # saliency_map = saliency(score, X)
    # Generate saliency map with smoothing that reduce noise by adding noise
    saliency_map = saliency(score,
                        X,
                        smooth_samples=20, # The number of calculating gradients iterations.
                        smooth_noise=0.20) # noise spread level.

        # Generate saliency map
    saliency_map = saliency(score, X)

    # Render
    # f, ax = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))
    plt.figure(figsize=(8,8))
    plt.imshow(saliency_map[0], cmap='jet', alpha=0.9)
    plt.axis('off')
    import os
    img_dir = './static/img/saliency'
    if (not os.path.isdir(img_dir)):
        os.mkdir(img_dir)

    plt.savefig(f'./static/img/saliency/{name}.svg', transparent=True)
    plt.close()

    return "Done"
    

if __name__ == "__main__":
    saliency()
