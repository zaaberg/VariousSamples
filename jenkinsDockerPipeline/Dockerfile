FROM ubuntu:xenial

LABEL maintainer="Zach Aaberg, aabe2458@stthomas.edu"

EXPOSE 8080

RUN apt-get update -y && apt-get install -y \
    python-dev \
    python-pip

COPY app/site.py /app/site.py

COPY app/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

ENTRYPOINT [ "python", "/app/site.py" ]
