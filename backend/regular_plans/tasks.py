import subprocess

from django.core.mail import BadHeaderError, send_mail

from backend.core.celery import app
from backend.core.settings import EMAIL_HOST_USER


@app.task
def send_email(subject, message, to_email):
    if subject and message and to_email:
        try:
            send_mail(subject, message, EMAIL_HOST_USER, [to_email])
        except BadHeaderError:
            return False
        return True
    else:
        return False


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


@app.task
def exports_to_mongo():
    subprocess.call("./pg2mongo.sh")
