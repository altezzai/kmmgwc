#!/bin/bash

# Activate the virtual environment
source /home/sn/kmmgwc/.venv/bin/activate

# Change to the directory where your Django project is located
cd /home/sn/kmmgwc

# Start Gunicorn using the configuration file (no need to repeat wsgi_app)
gunicorn -c gunicorn.conf.py

