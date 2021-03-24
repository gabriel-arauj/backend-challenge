from django.contrib.auth.models import  Group
from rest_framework import serializers
from .models import User
from ..regularplans.serializers import RegularPlanSerializer


class UserSerializer(serializers.ModelSerializer):
    regularplans = RegularPlanSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'username',]


