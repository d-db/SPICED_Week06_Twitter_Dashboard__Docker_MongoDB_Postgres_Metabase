# syntax=docker/dockerfile:1

FROM python:3.8-alpine

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN python3 -m nltk.downloader omw-1.4

CMD python get_tweets.py


