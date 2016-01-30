# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_ts',
            field=models.DateTimeField(),
        ),
    ]
