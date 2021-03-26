from pathlib import Path

from celery.schedules import crontab
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = config("SECRET_KEY", default="Change_me")

DEBUG = config("DEBUG", default=True, cast=bool)


ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_celery_beat",
    "backend.regular_plans",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.core.wsgi.application"

DB_NAME = config("DB_NAME", default="postgres")
DB_USER = config("DB_USER", default="postgres")
DB_PASSWORD = config("DB_PASSWORD", default="postgres")
DB_HOST = config("DB_HOST", default="db")
DB_PORT = config("DB_PORT", default="5432")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
    },
    "mongo_db": {
        "ENGINE": "djongo",
        "NAME": config("MONGO_INITDB_DATABASE", default="challengeproject"),
        "CLIENT": {
            "host": config("MONGO_DB_HOST", default="mongo"),
            "port": config("MONGO_DB_PORT", default=27017),
            "username": config("MONGO_INITDB_ROOT_USERNAME", default="root"),
            "password": config("MONGO_INITDB_ROOT_PASSWORD", default="example"),
            "authSource": config("MONGO_DB_AUTH", default="admin"),
        },
    },
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"

# Sending email settings

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_USE_TLS = True
EMAIL_PORT = config("EMAIL_PORT", default=587)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="Change_me")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="Change_me")

# Celery settings

CELERY_BROKER_URL = "pyamqp://rabbitmq:5672"
# running the task every 5 minutes for example purposes.
CELERY_BEAT_SCHEDULE = {
    "exports_to_mongoe_very_five_minutes": {
        "task": "backend.regular_plans.tasks.exports_to_mongo",
        "schedule": crontab(minute="*/5"),
    }
}
