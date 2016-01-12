# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Employer', '0002_auto_20160109_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
