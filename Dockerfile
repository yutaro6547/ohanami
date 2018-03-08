FROM python:3.6.4-stretch

WORKDIR /usr/src/app

RUN pip install --no-cache-dir slackbot websocket-client
COPY . .

CMD [ "python", "./run.py" ]
