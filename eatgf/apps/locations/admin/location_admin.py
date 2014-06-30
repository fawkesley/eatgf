from django.contrib import admin
from eatgf.apps.locations.models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
