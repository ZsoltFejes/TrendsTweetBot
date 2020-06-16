FROM python:3.8

RUN adduser --disabled-password bot

WORKDIR /home/bot

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt

COPY bot.py config.py boot.sh ./
RUN chmod +x boot.sh

RUN chown -R bot:bot ./
USER bot

ENTRYPOINT ["./boot.sh"]
