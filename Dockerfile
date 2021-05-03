# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.7-slim-buster
ARG CACHEBUST=1 
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
# libraries for opencv
RUN python -m pip install -r requirements.txt

# fetch models from drive
RUN gdown https://drive.google.com/uc?id=1Zs3xrGGKIAbq_3uDG5X2Sj6H2sUsPmB0 -O ./models/binary-model.h5
RUN gdown https://drive.google.com/uc?id=1LUJK_QVdWuZzJeOdsfg5R3F_OXLKt3rt -O ./models/multiclass-model.h5
RUN apt-get update

# install required linux dependencies
RUN apt install -y libglib2.0-0 libsm6 libxext6 libxrender-dev

RUN python -m pip install --upgrade --force-reinstall setuptools

WORKDIR /app
COPY . /app

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
EXPOSE 8000
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]

