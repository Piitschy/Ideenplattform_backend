#!/bin/sh

pkill -f gunicorn
deactivate
git pull origin master
source FlaskAppENV/bin/activate
gunicorn --bind 0.0.0.0:8080 wsgi:app
