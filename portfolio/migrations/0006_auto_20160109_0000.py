# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20160108_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workhistory',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
