# _*_ coding: utf-8 _*_
__author__ = 'Steven'
__date__ = '2017/8/20 21:55'

import xadmin
from xadmin import views
from users.models import Org


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = u"运营管理系统"
    site_footer = "CopyRight@steven 2017"
    menu_style = "accordion"


class OrgAdmin(object):
    list_display = ["name", "description", "parentID", "add_time"]
    search_fields = ["name", "description", "parentID", "add_time"]
    list_filter = ["name", "description", "parentID", "add_time"]

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Org, OrgAdmin)


