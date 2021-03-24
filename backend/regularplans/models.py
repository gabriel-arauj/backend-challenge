from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ..users.models import User

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