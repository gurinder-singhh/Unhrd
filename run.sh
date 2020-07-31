#!/bin/bash

# Author : Vishaljeet Singh

echo 'starting webapplication with gunicorn'

gunicorn -w 3 -b localhost:8000 unhrdmodule.wsgi
