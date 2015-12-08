# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zooguide', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animals',
            name='animal_text',
        ),
        migrations.RemoveField(
            model_name='exhibits',
            name='exhibit_text',
        ),
        migrations.AddField(
            model_name='animals',
            name='exhibit_name',
            field=models.TextField(default=b'default', max_length=35),
        ),
        migrations.AddField(
            model_name='exhibits',
            name='exhibit_awards',
            field=models.TextField(default=b'default', max_length=200),
        ),
        migrations.AddField(
            model_name='exhibits',
            name='exhibit_cost',
            field=models.TextField(default=b'default', max_length=35),
        ),
        migrations.AddField(
            model_name='exhibits',
            name='exhibit_date',
            field=models.TextField(default=b'default', max_length=35),
        ),
        migrations.AddField(
            model_name='exhibits',
            name='exhibit_ilink',
            field=models.TextField(default=b'default', max_length=200),
        ),
        migrations.AddField(
            model_name='exhibits',
            name='exhibit_latest',
            field=models.TextField(default=b'default', max_length=200),
        ),
        migrations.AlterField(
            model_name='tips',
            name='tip_text',
            field=models.TextField(),
        ),
    ]
