# _*_ coding: utf-8 _*_
__author__ = 'Steven'
__date__ = '2017/8/21 21:47'

import xadmin
from .models import BugetItem


class BugetItemAdmin(object):
    list_display = ["custom_id", "buget_type", "name", "desc", "standard",
                    "edit_dept", "approve_dept", "account_item", "add_user", "add_time"]
    search_fields = ["custom_id", "buget_type", "name", "desc", "standard",
                    "edit_dept", "approve_dept", "account_item", "add_user"]
    list_filter = ["custom_id", "buget_type", "name", "desc", "standard",
                    "edit_dept", "approve_dept", "account_item", "add_user", "add_time"]


xadmin.site.register(BugetItem, BugetItemAdmin)
