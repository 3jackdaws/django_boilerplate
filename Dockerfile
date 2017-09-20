FROM                    python:3.6
MAINTAINER              Ian Murphy <ian@isogen.net> #change this, obv

RUN                     mkdir /app

ADD                     . .

RUN                     pip3 install -r requirements.txt

EXPOSE                  80

VOLUME                  /app

ENTRYPOINT              bash -c 'bash docker-entrypoint.sh'