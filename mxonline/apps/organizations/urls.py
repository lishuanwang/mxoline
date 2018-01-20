# -*- coding:utf-8 -*-  
""" 
@author:python 
@file: urls.py 
@time: 2018/01/20/22/39 
"""

from django.conf.urls import url, include

from .views import  OrgListView


urlpatterns =[
    url(r'^list/$', OrgListView.as_view(), name='list'),
]
