# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0002_layer_current_version'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='layerversionmodel',
            name='layer',
        ),
        migrations.DeleteModel(
            name='LayerVersionModel',
        ),
    ]
