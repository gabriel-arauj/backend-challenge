#!/bin/sh
python manage.py dumpdata > dump.json
python manage.py migrate  --database=mongo_db --fake django_celery_beat
python manage.py migrate  --database=mongo_db 
python manage.py loaddata dump.json --database=mongo_db
rm dump.json
exec "$@"