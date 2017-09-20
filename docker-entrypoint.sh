#!/usr/bin/env bash

# do all the pre-start setup here

export PYTHONUNBUFFERED=TRUE #makes debugging quicker
gunicorn --reload -b "0.0.0.0:80" app.wsgi -k gevent -w 1 --graceful-timeout 2

# --reload: reloads the gunicorn server if file changes are detected
# --graceful-timeout: time in seconds workers are allowed to serve requests after a restart request, after, they are killed
