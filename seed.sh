#!/bin/bash

echo "dropping database django-birdspotter"
dropdb django-birdspotter

echo "creating database django-birdspotter"
createdb django-birdspotter

python manage.py makemigrations

python manage.py migrate

echo "inserting users"
python manage.py loaddata jwt_auth/seeds.json