from django.contrib import admin
from eatgf.apps.restaurants.models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass
