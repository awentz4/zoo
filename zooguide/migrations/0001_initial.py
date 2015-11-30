# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('animal_name', models.CharField(max_length=35)),
                ('animal_text', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Exhibits',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exhibit_name', models.CharField(max_length=35)),
                ('exhibit_text', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tip_title', models.CharField(max_length=35)),
                ('tip_text', models.CharField(max_length=250)),
            ],
        ),
    ]
