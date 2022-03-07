FROM python:3.9

RUN apt update

RUN python -m pip install python-telegram-bot

COPY . /app

WORKDIR /app

CMD [ "python", "TeleBot.py" ]