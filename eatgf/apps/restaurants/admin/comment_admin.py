from django.contrib import admin
from eatgf.apps.restaurants.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'restaurant', 'author', 'created')
