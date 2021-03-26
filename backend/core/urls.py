from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from backend.regular_plans.views import RegularPlanViewSet

router = routers.DefaultRouter()
router.register(r"regular-plans", RegularPlanViewSet, basename="regular-plans")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include(router.urls)),
]
