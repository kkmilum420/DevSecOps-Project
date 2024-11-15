#!/bin/bash

# Activate the virtual environment
source /home/site/wwwroot/refApp/Scripts/activate

# Start the Gunicorn server
gunicorn --chdir /home/site/wwwroot ref_WebApplication.wsgi:application --bind 0.0.0.0:8000
#gunicorn --bind=0.0.0.0 --timeout 600 