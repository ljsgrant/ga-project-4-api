#!/bin/bash

echo "creating jwt_auth/seeds.json"
python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;
echo "creating birds/seeds.json"
python manage.py dumpdata birds --output birds/seeds.json --indent=2;
echo "creating sightings/seeds.json"
python manage.py dumpdata sightings --output sightings/seeds.json --indent=2;