from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from backend.users.models import User
from .tasks import send_email



class RegularPlan(models.Model):
    CYCLE_CHOICES = (
        ('W', 'Weekly'),
        ('D', 'Daily')
    )
    TYPE_CHOICES = (
        ('bi', 'bi-time'),
        ('tri', 'tri-time'),
        ('simple', 'simple')
    )
    UNIT_CHOICES = (
        ('KWH', 'kwh'),
        ('MIN', 'min')
    )
    name = models.CharField('Name', max_length=255)
    tar_included = models.BooleanField()
    subscription = models.FloatField()
    cycle = models.CharField(max_length=1, choices=CYCLE_CHOICES, blank=False, null=False)
    type = models.CharField(max_length=6, choices=TYPE_CHOICES, blank=False, null=False)
    offer_iva = models.BooleanField()
    off_peak_price = models.FloatField()
    peak_price = models.FloatField()
    unit = models.CharField(max_length=3, choices=UNIT_CHOICES, blank=False, null=False)
    valid = models.BooleanField()
    publish = models.BooleanField()
    vat = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="plans")

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(RegularPlan, self).__init__(*args, **kwargs)
        self.old_publish = self.publish

    def save(self, **kwargs):
        # Check if publish changed to True and send a email
        add.delay(1,1)
        if self.publish == True:
            if self.old_publish != self.publish or self.id == None:
                subject = f"Your Regular Plan:{self.name} has been published"
                message = f"Hello, {self.owner.username}\n\n Your Regular Plan: {self.name} has been published!"
                to_email = self.owner.email
                send_email.delay(subject, message, to_email)
        super().save(**kwargs)