from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

from eatgf.libs.strict_slug import STRICT_SLUG_VALIDATOR


@python_2_unicode_compatible
class Location(models.Model):
    class Meta:
        app_label = 'locations'

    slug = models.SlugField(
        max_length=100,
        unique=True,
        validators=[STRICT_SLUG_VALIDATOR])

    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name
