FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update
RUN apt-get install gcc default-libmysqlclient-dev -y

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT [ "bash", "/usr/local/bin/docker-entrypoint.sh" ]