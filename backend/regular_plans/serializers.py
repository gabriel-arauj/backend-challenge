from rest_framework import serializers

from .models import RegularPlan


class RegularPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegularPlan
        fields = "__all__"
