# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user_name', models.CharField(blank=True, max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('bio', models.TextField(verbose_name='About You', max_length=500)),
                ('profile_picture', models.ImageField(upload_to='', blank=True)),
                ('website_url', models.URLField(null=True)),
                ('years_exp', models.IntegerField(verbose_name='Years of experience', default=1, blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)])),
                ('software_title', models.CharField(default='Back-End', blank=True, max_length=50)),
                ('languages', models.CharField(verbose_name='Programming Languages', blank=True, max_length=1000)),
                ('is_developer', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='portfolios', blank=True)),
                ('description', models.TextField()),
                ('github_link', models.URLField()),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to='Register_Developer.Developer')),
            ],
        ),
    ]
