#!/bin/sh

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser if it doesn't exist
python manage.py createsuperuser --no-input --username admin --email admin@test.com || echo "Superuser already exists"

# Import menu data
python manage.py import_menu_data ./utils/data/menu_data.json

# Start the Django server
exec "$@"