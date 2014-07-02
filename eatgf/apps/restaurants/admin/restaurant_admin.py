from django.contrib import admin
from eatgf.apps.restaurants.models import Restaurant

from ..models import Comment


class CommentInline(admin.TabularInline):
    model = Comment
    can_delete = True


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'slug', 'website')
    inlines = [CommentInline]
