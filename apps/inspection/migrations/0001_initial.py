# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-20 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='greenlane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum_year', models.IntegerField(default=0, max_length=20, verbose_name='\u5e74\u5ea6')),
                ('sum_mon', models.IntegerField(default=0, max_length=20, verbose_name='\u6708\u5ea6')),
                ('roadname', models.CharField(default='', max_length=30, verbose_name='\u8def\u6bb5')),
                ('stationname', models.CharField(default='', max_length=30, verbose_name='\u7ad9\u573a')),
                ('flow_BS', models.IntegerField(default=0, max_length=20, verbose_name='\u62c6\u524d\u7eff\u901a\u8f66\u6d41\u91cf')),
                ('money_BS', models.IntegerField(default=0, max_length=40, verbose_name='\u62c6\u524d\u7eff\u901a\u51cf\u514d\u989d')),
                ('flow_AS', models.IntegerField(default=0, max_length=20, verbose_name='\u62c6\u524d\u7eff\u901a\u8f66\u6d41\u91cf')),
                ('money_AS', models.IntegerField(default=0, max_length=40, verbose_name='\u62c6\u524d\u7eff\u901a\u51cf\u514d\u989d')),
                ('chargeflow_BS', models.IntegerField(default=0, max_length=20, verbose_name='\u62c6\u524d\u6536\u8d39\u7eff\u901a\u6d41\u91cf')),
                ('chargemoney_BS', models.IntegerField(default=0, max_length=40, verbose_name='\u62c6\u524d\u6536\u8d39\u7eff\u901a\u91d1\u989d')),
                ('truckflow_BS', models.IntegerField(default=0, max_length=20, verbose_name='\u62c6\u524d\u8d27\u8f66\u6d41\u91cf')),
                ('addusername', models.CharField(default='', max_length=30, verbose_name='\u586b\u62a5\u4eba')),
                ('addtime', models.TimeField(default='', max_length=30, null=True, verbose_name='\u586b\u62a5\u65f6\u95f4')),
                ('temp1', models.CharField(default='', max_length=30, verbose_name='\u5907\u75281')),
                ('temp2', models.CharField(default='', max_length=30, verbose_name='\u5907\u75282')),
            ],
            options={
                'verbose_name': '\u7eff\u901a\u6708\u62a5',
                'verbose_name_plural': '\u7eff\u901a\u6708\u62a5',
            },
        ),
    ]