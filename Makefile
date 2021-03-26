migrate:
	python manage.py makemigrations
	python manage.py migrate

test:
	python manage.py test backend/regularplans/

createsuperuser:
	python manage.py createsuperuser

runserver:
	python manage.py runserver 0.0.0.0:8000

celery:
	celery -A backend.core.celery worker -l info -B