FROM alpine:latest

RUN apk --update add python3 py3-pip

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]
