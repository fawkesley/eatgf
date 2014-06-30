from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

from eatgf.apps.locations.models import Location
from eatgf.libs.strict_slug import STRICT_SLUG_VALIDATOR


@python_2_unicode_compatible
class Restaurant(models.Model):
    class Meta:
        app_label = 'restaurants'

    slug = models.SlugField(
        max_length=100,
        unique=True,
        validators=[STRICT_SLUG_VALIDATOR])

    name = models.CharField(max_length=200, blank=False)

    location = models.ForeignKey(
        Location,
        related_name='restaurants',
        on_delete=models.PROTECT)

    def __str__(self):
        return self.name
