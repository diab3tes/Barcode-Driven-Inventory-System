#!/bin/bash
echo "Building project..."
set -o errexit
echo "Installing dependencies..."
pip install -r requirements.txt
python manage.py collectstatic --no-input

echo "Running build..."
python manage.py build