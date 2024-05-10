#!/bin/bash

if [ -f /app/env/.env ]; then
    source /app/env/.env
fi

python manage.py makemigrations

python manage.py migrate -v 2
# python manage.py test
# python manage.py runserver 0.0.0.0:8000

