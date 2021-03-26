from django.contrib import admin

from .models import RegularPlan


class RegularPlanAdmin(admin.ModelAdmin):
    model = RegularPlan
    list_display = ["id", "name", "subscription", "publish", "valid"]
    list_filter = ("name", "subscription", "publish", "valid")
    list_display_links = ("id", "name")


admin.site.register(RegularPlan, RegularPlanAdmin)
