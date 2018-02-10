# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layerversionmodel',
            name='version',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
