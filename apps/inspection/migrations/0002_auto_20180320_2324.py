# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-20 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greenlane',
            name='chargeflow_BS',
            field=models.IntegerField(default=0, verbose_name='\u62c6\u524d\u6536\u8d39\u7eff\u901a\u6d41\u91cf'),
        ),
        migrations.AlterField(
            model_name='greenlane',
            name='chargemoney_BS',
            field=models.IntegerField(default=0, verbose_name='\u62c6\u524d\u6536\u8d39\u7eff\u901a\u91d1\u989d'),
        ),
        migrations.AlterField(
            model_name='greenlane',
            name='flow_AS',
            field=models.IntegerField(default=0, verbose_name='\u62c6\u524d\u7eff\u901a\u8f66\u6d41\u91cf'),
        ),
        migrations.AlterField(
            model_name='greenlane',
            name='flow_BS',
            field=models.IntegerField(default=0, verbose_name='\u62c6\u524d\u7eff\u901a\u8f66\u6d41\u91cf'),
        ),
        migrations.AlterField(
            model_name='greenlane',
            name='money_AS',
            field=models.IntegerField(default=0, verbose_name='\u62c6\u524d\u7eff\u901a\u51cf\u514d\u989d'),
        ),
        migrations.AlterField(
            model_name='greenlane',
            name='money_BS',
            field=models.IntegerField(default=0, verbose_name='\u62c6\u524d\u7eff\u901a\u51cf\u514d\u989d'),
        ),
        migrations.AlterField(
            model_name='greenlane',
            name='sum_mon',
            field=models.IntegerField(default=0, verbose_name='\u6708\u5ea6'),
        ),
        migrations.AlterField(
            model_name='greenlane',
            name='sum_year',
            field=models.IntegerField(default=0, verbose_name='\u5e74\u5ea6'),
        ),
        migrations.AlterField(
            model_name='greenlane',
            name='truckflow_BS',
            field=models.IntegerField(default=0, verbose_name='\u62c6\u524d\u8d27\u8f66\u6d41\u91cf'),
        ),
    ]
