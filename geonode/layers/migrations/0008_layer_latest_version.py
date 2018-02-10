# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0007_layerversionmodel_version_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='latest_version',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
