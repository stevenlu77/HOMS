# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.

class greenlane(models.Model):
    sum_year = models.IntegerField(null=False, verbose_name=u"年度", default=0)
    sum_mon = models.IntegerField(null=False, verbose_name=u"月度", default=0)
    roadname = models.CharField(max_length=30, null=False, verbose_name=u"路段", default="")
    stationname = models.CharField(max_length=30, null=False, verbose_name=u"站场", default="")
    flow_BS = models.IntegerField(null=False, verbose_name=u"拆前绿通车流量", default=0)
    money_BS = models.IntegerField(null=False, verbose_name=u"拆前绿通减免额", default=0)
    flow_AS = models.IntegerField(null=False, verbose_name=u"拆前绿通车流量", default=0)
    money_AS = models.IntegerField(null=False, verbose_name=u"拆前绿通减免额", default=0)
    chargeflow_BS = models.IntegerField(null=False, verbose_name=u"拆前收费绿通流量", default=0)
    chargemoney_BS = models.IntegerField(null=False, verbose_name=u"拆前收费绿通金额", default=0)
    truckflow_BS = models.IntegerField(null=False, verbose_name=u"拆前货车流量", default=0)
    addusername = models.CharField(max_length=30, null=False, verbose_name=u"填报人", default="")
    addtime = models.TimeField(max_length=30, null=True, verbose_name=u"填报时间", default="")
    temp1 = models.CharField(max_length=30, null=False, verbose_name=u"备用1", default="")
    temp2 = models.CharField(max_length=30, null=False, verbose_name=u"备用2", default="")

    class Meta:
        verbose_name = u"绿通月报"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name