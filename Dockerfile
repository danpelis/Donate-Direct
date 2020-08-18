# Dockerfile
FROM python:3.7-stretch
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip uninstall bson
RUN pip uninstall pymongo
RUN pip install pymongo
ENTRYPOINT ["python"]
CMD ["main.py"]