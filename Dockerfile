FROM python:3.8
WORKDIR /app
RUN apt-get update && apt-get install -y 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "run.py"]
