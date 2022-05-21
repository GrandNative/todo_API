FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update \
    && apk add --virtual build-deps gcc python3 python3-dev mariadb-dev build-base musl-dev libc-dev && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base
RUN apk add zlib-dev jpeg-dev
RUN apk add  --no-cache ffmpeg
RUN apk add netcat-openbsd
RUN apk add libffi-dev

WORKDIR /todo
COPY . .
COPY requirements.txt requirements.txt
Run python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 8000

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]
#CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]