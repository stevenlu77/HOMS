# _*_ coding: utf-8 _*_
import xadmin
from xadmin import views
from inspection.models import greenlane

__author__ = 'Steven'
__date__ = '2018/3/20 23:26'

class GreenLaneAdmin(object):
    list_display = ["sum_year", "sum_mon", "roadname", "stationname"]
    search_fields = ["sum_year", "sum_mon", "roadname", "stationname"]
    list_filter = ["sum_year", "sum_mon", "roadname", "stationname"]
    model_icon = 'fa fa-sitemap'

    # def save_models(self):
    #     self.new_obj.addusername = self.request.addusername
    #     super().save_models()


xadmin.site.register(greenlane, GreenLaneAdmin)