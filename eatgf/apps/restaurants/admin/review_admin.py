from django.contrib import admin
from eatgf.apps.restaurants.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'restaurant', 'author', 'created')
