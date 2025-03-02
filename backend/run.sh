#!/bin/bash
export INFISICAL_TOKEN=$(cat /run/secrets/infisical_token)
infisical run --env=dev --path="/To-do-app/backend" -- sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
