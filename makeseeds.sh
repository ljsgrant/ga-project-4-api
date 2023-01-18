#!/bin/bash

echo "creating jwt_auth/seeds.json"
python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;