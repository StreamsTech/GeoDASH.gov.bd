# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0006_auto_20180209_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='layerversionmodel',
            name='version_path',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
