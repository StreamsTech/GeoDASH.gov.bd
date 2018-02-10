# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='download_count',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='layer',
            name='file_size',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
