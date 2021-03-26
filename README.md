
# API to manage Regular Plans

## []()Getting Started:

## Run with Docker

```
docker-compose up -d --build
```

> Access in: [http://localhost:8000/](http://localhost:8000/)

## Run Locally

### []()Prerequisites

```
Python3
Pip
Virtual environment python
Django
Django Rest Framework
Celery
RabbitMQ
```

Activate your virtual environment before proceeding with the installation.


### []()Installing

To install the requirements:

```
pip install -r requirements.txt
```

To do database migrations:

```
make migrate
```

To run the Rest API:

```
python manage.py runserver
```

> Access in: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## []()Running the tests

To run the tests:

```
make test
```

## []()Create Super User

To create a super user:

```
make createsuperuser
```

provide username, email and password when prompted.

## []()Activate Celery
first you need to install [RabbitMQ](https://www.rabbitmq.com/).

Then start celery:
```
make celery
```

## []()Built With

- [Django Rest Framework](https://www.django-rest-framework.org/)

# REST API

## Endpoints:

#### Authentication
First you need to authenticate yourself to be able to do anything. Use the meke createsuperuser to create a user.
`/api-auth/login/`

#### List Regular Plans
lists all plans owned by the user

`GET /regularplans`

lists all plans with publish=true

`GET /regularplans?publish=true`

#### Create a Regular Plan
Create Regular Plan for the the User

`POST /regularplans`

```json
{
    "id": 1,
    "name": "Plan 1",
    "tar_included": true,
    "subscription": 12.0,
    "cycle": "W",
    "type": "bi",
    "offer_iva": true,
    "off_peak_price": 4.0,
    "peak_price": 4.0,
    "unit": "KWH",
    "valid": true,
    "publish": true,
    "vat": 44,
    "owner": 1
    }
```
#### Detail Regular Plan
Show information for a Regular plan owned by the user
`GET /regularplans/:id/`

Update information for a Regular plan owned by the user
`PUT /regularplans/:id/`
# Improvements:

- django structure patterns and code style

# Challenge
- create a Django project with a CRUD using a Regular Plan Model:
    -  id: the identifier of the plan
    - name: the name of the plan, readable for the user
    - tar_included: a boolean field
    - subscription: float, it’s the monthly subscription for the user
    - cycle: if it’s daily or weekly
    - type: bi-time, tri-time, simple
    - offer_iva: boolean true or false
    - off_peak_price: float
    - peak_price: float
    - unit: kwh or min
    - valid: true or false
    - publish: true or false
    - vat: 1 to 100
    - owner: can be null if publish is true or false
- List API RegularPlans with publish True;
- Create Regular Plan for the the User;
- List Regular Plan for the user;
- Update information for a Regular plan owned by the user;
- Use docker compose to launch a Mongo database, and create a cronjob that exports
this information to a collection, protecting the User sensitive information;
- Send a e-mail when publish is True with Celery.


