from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import RegularPlanSerializer
from .models import RegularPlan


class RegularPlanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that list Regular Plans.
    """
    serializer_class = RegularPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.GET.get('publish', None) == 'true':
            return RegularPlan.objects.filter(publish=True)
        return self.request.user.plans.all()
    
    def retrieve(self, request, pk=None):
        queryset = RegularPlan.objects.all()
        regularplan = get_object_or_404(queryset, pk=pk)
        if regularplan.publish == True or regularplan.owner == self.request.user:
            return Response(RegularPlanSerializer(regularplan).data)
        return Response({"detail": "Not found."})
            

