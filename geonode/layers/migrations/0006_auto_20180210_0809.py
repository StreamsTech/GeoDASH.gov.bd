# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0005_auto_20180210_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='file_size',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
