# Abstract
AI and Machine Learnings use in detecting pulmonary disorders such as Tuberculosis, pneumonia and many others has been a well-known fact for quite a while now. When — Coronavirus disease 2019 also known as COVID-19 was declared as a pandemic in 2020 those similar techniques could be used for the diagnosis of COVID-19, especially in developing countries where there is lack of specialized physicians, and test kits are in scarce supply. These inadequacies are leading to the misdiagnosis of the different pulmonary disorders, more specifically COVID-19. The objective of this project is to provide an overview on the use of Deep neural networks, both Vanilla neural networks and other pretrained models to present a quick solution to provide a classification between COVID-19, Bacterial Pneumonia, viral Pneumonia, Tuberculosis, and Normal/Healthy images. In this effort.

It is critical to detect the positive cases as early as possible so as to prevent the further spread of this pandemic and to quickly treat affected patients. The need for auxiliary diagnostic tools has increased as there are no accurate automated toolkits available. 

Recent findings obtained using radiology imaging techniques suggest that such images contain salient information about the COVID-19 virus. Application of advanced artificial intelligence (AI) techniques coupled with radiological imaging can be helpful for the accurate detection of this disease, and can also be assistive to overcome the problem of a lack of specialized physicians in remote villages. 

# Objective
Given X-ray images of patients, to build a machine learning model that will analyze and detect if the patient has COVID-19 or not and also classify between 3 other pulmonary Disorders Tuberculosis, Bacterial, and Viral Pneumonia.

*This may not be clinically viable*

# Usage
## Option 1: Docker
This is a containerized flask application with docker image put on docker hub. If azure url is not working 
Pull docker image
```
docker pull 0941924816/covid-detection-or-analysis:latest
```
Run docker image
```
docker run 0941924816/covid-detection-or-analysis:latest
```

## Option 2:(no docker)
If you do not have docker installed make sure you have python3 and pip3 installed
<br>

**1. Clone the repo**
```
git clone https://github.com/Azariagmt/pulmonary-disorder-detection-using-x-ray-images.git
```
**2. cd into repo**
```
cd pulmonary-disorder-detection-using-x-ray-images
```
**3.Install required dependencies:**
```
pip3 install requirements.txt
```
**4.Run Flask application**
```
python3 run app.py
```

# Datasets
The datasets utilized in this project are obtained from three publicly available sources. The first one is the Covid-19 Chest X-ray Database (Rahman et al.) which in its current version consists of 3616 COVID-19 positive cases along with 10,192 Normal, 6012 Lung Opacity (Non-COVID lung infection), and 1345 Viral Pneumonia images. The second one is the Chest X-Ray Images (Pneumonia) dataset (Mooney) consisting of 5,863 X-Ray images split into 2 categories (Pneumonia/Normal). The third dataset used is The Tuberculosis (TB) Chest X-ray Database (Rahman #) which contains CXR images of Normal (3500) and patients with TB (3500).
___

# Repository structure

### Numpy Arrays
Stored numpy arrays in .npz and .npy extension can be found in /numpy arrays directory
### Notebooks
Trained models using data code and results is found in notebooks dir(/notebooks)

### Flask Application
The flask application for this app is instantiated in app.py

Pulmonary disorder detection repository 
	├── models (fetched from google drive)
	├── modules	
	│   ├── load_models.py (fetches models)
	│   ├── predict.py
	├── notebooks	
	│   ├── Data Fetching and preprocessing
	│   ├   ├── Get datasets.ipynb
	│   ├   ├── Data preprocessing.ipynb
    |   └── Training
    │       ├── DenseNet201.ipynb
    │       ├── InceptionResNetV2.ipynb
    │       ├── InceptionV3.ipynb
    │       ├── NasNetLarge.ipynb
    │       ├── ResNet101V2.ipynb
    │       ├── ResNet50V2.ipynb
    │       ├── VGG19.ipynb
    │       ├── Xception.ipynb
	├── numpy arrays
	├── static
	├── templates
    ├── app.py
    ├── Dockerfile


# Results
Transfer learning was used in the building of the models, some reaching an accuracy of 98.4% on the dataset collected from the different sources above.
## Confusion matrix for chosen models
These are the confusion matrices of tsome of the pretrained models used to build the models.
### Xception
![Confusion matrix for Xception](static/readme%20assets/confusion-matrix-Xception.png)
### DenseNet201
![Confusion matrix for Xception](static/readme%20assets/confusion-matrix-DenseNet.png)
### ResNet50V2
![Confusion matrix for Xception](static/readme%20assets/confusion-matrix-ResNet50V2.png)

# Conclusion
This project has several limitations that can be overcome in future research. In particular, a more in-depth analysis requires much more patient data, especially those suffering from COVID-19(currently) and more research for the specific pulmonary disorder we're trying to predict in an area. A more interesting approach for future research would focus on distinguishing patients showing mild symptoms, and those that will actually need intubation or not. while these symptoms may not be accurately visualized on X-rays, or may not be visualized at all.

Furthermore, we will try to use our approach on bigger datasets, to solve other medical problems like cancer, tumors, etc. and also on other computer vision fields as energy, agriculture, and transport in the upcoming days. Future research directions will include the exploration of image data augmentation techniques to improve accuracy even more while avoiding overfitting. We observed that performance could be improved further, by increasing dataset size, using a data augmentation approach, and using hand-crafted features, in the future. More models will be trained and the different architectures of the pretrained models will also be analyzed further!
