# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-24 14:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='ratings', to=settings.AUTH_USER_MODEL, verbose_name='\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
        ),
    ]