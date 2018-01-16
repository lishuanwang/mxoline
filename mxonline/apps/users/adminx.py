# -*- coding:utf-8 -*-
""" 
@author:python 
@file: adminx.py 
@time: 2018/01/14/23/20 
"""
import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学网"
    # menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']


class BannerAdmin(object):

    list_display = ['title', 'url', 'image', 'index']
    list_filter = ['title', 'url', 'image', 'index', 'add_time']
    search_fields = ['title', 'url', 'image', 'index']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
