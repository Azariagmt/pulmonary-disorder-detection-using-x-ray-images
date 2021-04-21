# Notebooks for the multiclass classification  models are found here
## Steps to replicate model training on own machine
## 1. Clone the repository
```
git clone https://github.com/Azariagmt/pulmonary-disorder-detection-using-x-ray-images.git
```
## 2. Run Get Datasets notebook
This step can now be skipped as the numpy arrays already come with the repository!
This will do a couple of things
* get the datasets from the sources cited in the main readme file and create a new directory /datasets on root and extract the datasets
* Save the numpy array's of the datasets in the `/numpy arrays` directory and get it ready for preprocessing.

## 3. Run individual notebook
if you're using the command line:
```
pip install runipy
``` 
runipy will run all cells in a notebook. If an error occurs, the process will stop.
```
runipy MyNotebook.ipynb
```
Command to save the output file as a notebook:
```
runipy MyNotebook.ipynb OutputNotebook.ipynb
```
! training requires a lot of compute power so make sure you have the necessary compute before retraining the models.