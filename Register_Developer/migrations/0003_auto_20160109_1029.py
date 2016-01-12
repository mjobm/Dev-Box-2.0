# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Developer', '0002_auto_20160107_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
