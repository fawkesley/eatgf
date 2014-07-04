from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.contrib.auth.models import User

from .restaurant import Restaurant


@python_2_unicode_compatible
class Review(models.Model):
    class Meta:
        app_label = 'restaurants'

    created = models.DateTimeField(editable=False)

    text = models.CharField(max_length=200, blank=False)

    restaurant = models.ForeignKey(
        Restaurant,
        related_name='reviews',
        on_delete=models.PROTECT)

    author = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = now()
        return super(Review, self).save(*args, **kwargs)

    def __str__(self):
        if len(self.text) > 20:
            return self.text[0:17] + '...'
        else:
            return self.text
