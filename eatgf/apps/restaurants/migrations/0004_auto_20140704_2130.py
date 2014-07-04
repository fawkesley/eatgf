# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_comment'),
    ]

    operations = [
        migrations.RenameModel('Comment', 'Review')
    ]
