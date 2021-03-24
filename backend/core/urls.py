
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend.regularplans.views import RegularPlanViewSet

router = routers.DefaultRouter()
router.register(r'regularplans', RegularPlanViewSet, basename="regularplans")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
