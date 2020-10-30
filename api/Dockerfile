FROM python:3.8
WORKDIR /api
RUN apt-get update
COPY . /api
RUN pip install -r requirements.txt

CMD ["python", "api.py"]

