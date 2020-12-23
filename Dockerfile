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
RUN python -m pip install googledrivedownloader
RUN python -m pip install gdown 
RUN apt-get update
RUN apt-get -y install libglib2.0-0
RUN apt install -y libsm6 libxext6
RUN apt-get install -y libxrender-dev
RUN python -m pip install --upgrade --force-reinstall setuptools

RUN echo "hello"
WORKDIR /app
COPY . /app

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
EXPOSE 8000
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]

