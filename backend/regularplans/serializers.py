from django.contrib.auth.models import  Group
from .models import RegularPlan
from rest_framework import serializers


class RegularPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegularPlan
        fields = '__all__'

