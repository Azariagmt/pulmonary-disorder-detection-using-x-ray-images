# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster


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

WORKDIR /app
COPY . /app

EXPOSE 8000
# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
# RUN useradd appuser && chown -R appuser /app
# USER appuser
RUN echo "change"
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]
# start flask app using Gunicorn
# CMD gunicorn -w 4 -b :8000 app:app
