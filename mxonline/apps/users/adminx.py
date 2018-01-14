# -*- coding:utf-8 _*-
""" 
@author:python 
@file: adminx.py 
@time: 2018/01/14/23/20 
"""
import xadmin
from .models import EmailVerifyRecord, Banner


class EmailVerifyRecordAdmin(object):
    pass

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
