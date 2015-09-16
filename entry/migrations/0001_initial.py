# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('job', models.CharField(max_length=50)),
                ('abbr', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='IsIt',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ch_tm', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('dt', models.DateField(verbose_name='At date')),
                ('doctor', models.ForeignKey(to='entry.Doctor')),
                ('tm', models.ForeignKey(to='entry.IsIt', verbose_name='At time')),
            ],
        ),
    ]
