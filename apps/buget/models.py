# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from users.models import UserProfile

# Create your models here.


class BugetItem(models.Model):   # 预算科目表
    custom_id = models.CharField(verbose_name=u"自定义ID", max_length=128)
    buget_type = models.CharField(verbose_name=u"类别", choices=(("expressway", u"高速公路经营"), ("build", u"高速公路建设"),
                                           ("cunstruction", u"施工企业"), ("investment", u"资产投资")), max_length=30)
    name = models.CharField(verbose_name=u"名称", max_length=255)
    desc = models.CharField(verbose_name=u"预算说明", null=True, blank=True, max_length=255)
    standard = models.CharField(verbose_name=u"预算定额", null=True, blank=True, max_length=255)
    edit_dept = models.CharField(verbose_name=u"编制部门", null=True, blank=True, max_length=255)
    approve_dept = models.CharField(verbose_name=u"审核部门", null=True, blank=True, max_length=255)
    account_item = models.CharField(verbose_name=u"财务科目", null=True, blank=True, max_length=255)
    add_user = models.ForeignKey(UserProfile, verbose_name=u"添加用户")
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)
    bk1 = models.CharField(verbose_name=u"备用1", null=True, blank=True, max_length=255)
    bk2 = models.CharField(verbose_name=u"备用2", null=True, blank=True, max_length=255)
    bk3 = models.CharField(verbose_name=u"备用3", null=True, blank=True, max_length=255)
    bk4 = models.CharField(verbose_name=u"备用4", null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = u"预算科目"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
