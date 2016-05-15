# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blockEvents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TimeFrom', models.DateTimeField(verbose_name=b'date published')),
                ('TimeTo', models.DateTimeField(verbose_name=b'date published')),
                ('Description', models.CharField(max_length=1000)),
                ('Responsible', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='blockMatList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numberOf', models.IntegerField(default=0)),
                ('responsible', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralMat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numberOf', models.IntegerField(default=1)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('storeDestination', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Picasso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Position', models.CharField(max_length=30)),
                ('Title', models.CharField(max_length=50)),
                ('Type', models.CharField(max_length=2)),
                ('Destination', models.CharField(max_length=50)),
                ('TimekDate', models.DateTimeField(verbose_name=b'date published')),
                ('TargetGroup', models.CharField(max_length=15)),
                ('Responsibles', models.CharField(max_length=35)),
                ('Atachements', models.CharField(max_length=50)),
                ('SpecialSecurity', models.BooleanField()),
                ('LinkToSecurity', models.CharField(max_length=100)),
                ('LinkToAlternative', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='blockmatlist',
            name='item',
            field=models.ForeignKey(to='lagerplaner.GeneralMat'),
        ),
        migrations.AddField(
            model_name='blockmatlist',
            name='mat',
            field=models.ForeignKey(to='lagerplaner.Picasso'),
        ),
        migrations.AddField(
            model_name='blockevents',
            name='event',
            field=models.ForeignKey(to='lagerplaner.Picasso'),
        ),
    ]
