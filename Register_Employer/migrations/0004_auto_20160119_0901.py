# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Employer', '0003_auto_20160109_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobpost',
            old_name='employer',
            new_name='owner',
        ),
    ]
