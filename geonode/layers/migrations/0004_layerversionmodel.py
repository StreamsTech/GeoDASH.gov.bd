# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0003_auto_20180207_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='LayerVersionModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.FloatField(null=True, blank=True)),
                ('version_name', models.CharField(max_length=400, null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('layer', models.ForeignKey(blank=True, to='layers.Layer', null=True)),
            ],
        ),
    ]
