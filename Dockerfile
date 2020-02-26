# base image from hub.docker.com
FROM python:3.7

COPY . /app
WORKDIR /app
RUN pip install --upgrade -r requirements.txt
RUN apt-get update && apt-get install -y ffmpeg
CMD [ "python", "./dl.py" ]

