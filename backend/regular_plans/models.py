from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .choices import CYCLE_CHOICES, TYPE_CHOICES, UNIT_CHOICES
from .tasks import send_email


class RegularPlan(models.Model):
    name = models.CharField(max_length=255)
    tar_included = models.BooleanField()
    subscription = models.FloatField()
    cycle = models.CharField(
        max_length=1, choices=CYCLE_CHOICES, blank=False, null=False
    )
    type = models.CharField(max_length=6, choices=TYPE_CHOICES, blank=False, null=False)
    offer_iva = models.BooleanField()
    off_peak_price = models.FloatField()
    peak_price = models.FloatField()
    unit = models.CharField(max_length=3, choices=UNIT_CHOICES, blank=False, null=False)
    valid = models.BooleanField()
    publish = models.BooleanField()
    vat = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="plans"
    )

    def __str__(self):
        return self.name


@receiver(pre_save, sender=RegularPlan)
def check_publish_true(sender, instance, **kwargs):
    """ Check if publish changed to True and send a email """

    if instance.publish and (
        not instance.id
        or instance.publish != RegularPlan.objects.get(pk=instance.id).publish
    ):
        subject = f"Your Regular Plan:{instance.name} has been published"
        message = f"Hello, {instance.owner.username}\n\n Your Regular Plan: {instance.name} has been published!"
        to_email = instance.owner.email
        send_email.delay(subject, message, to_email)
