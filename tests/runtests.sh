#!/bin/sh

export DJANGO_MANAGE=manage.py
export args="$@"

python $DJANGO_MANAGE test rest_framework_bulk "$args"
