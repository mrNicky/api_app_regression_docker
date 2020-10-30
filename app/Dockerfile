FROM python:3.8
WORKDIR /app
RUN apt-get update
COPY . /app
RUN pip install -r requirements.txt

CMD ["python", "main.py"]


