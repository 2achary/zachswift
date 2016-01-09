# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_contact_data_deployment_education_general_os_references_testing_workhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workhistory',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]
