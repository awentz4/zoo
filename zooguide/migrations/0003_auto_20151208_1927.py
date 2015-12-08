# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zooguide', '0002_auto_20151208_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Tips',
        ),
        migrations.AddField(
            model_name='exhibits',
            name='animals',
            field=models.ManyToManyField(to='zooguide.Animals', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='exhibits',
            name='description',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='animals',
            name='exhibit_name',
            field=models.CharField(default=b'default', max_length=35),
        ),
        migrations.AlterField(
            model_name='exhibits',
            name='exhibit_awards',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='exhibits',
            name='exhibit_cost',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='exhibits',
            name='exhibit_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='exhibits',
            name='exhibit_ilink',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='exhibits',
            name='exhibit_latest',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='location',
            field=models.ManyToManyField(to='zooguide.Exhibits', null=True, blank=True),
        ),
    ]
