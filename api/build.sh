#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip3 install -r requirements.txt

# Static files always need to be collected
python3 manage.py collectstatic --no-input

# # Apply model changes - this is safe and won't reset data
# echo "Running makemigrations..."
# python manage.py makemigrations challenges --no-input

# Run migrations - this updates schema but preserves data
echo "Running migrate..."
python3 manage.py migrate --no-input

echo "Build script completed successfully."
