FROM python:3.12-slim-bookworm

WORKDIR /app

COPY . .

RUN apt update && apt upgrade -y && \
pip install --no-cache-dir -r requirements.txt && \
rm requirements.txt && \
useradd -s /bin/bash youtube && \
chown -R youtube:youtube /app && \
chmod -R 770 /app && \
pip install --upgrade pytubefix colorama

ENV PYTHONPATH=/usr/local/bin

USER youtube

ENTRYPOINT [ "python", "choose.py" ]
