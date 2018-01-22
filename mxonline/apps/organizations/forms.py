# -*- coding:utf-8 -*-  
""" 
@author:python 
@file: forms.py 
@time: 2018/01/20/22/49 
"""
import re

from django import forms
from django.forms.models import ModelForm

from operation.models import UserAsk


class AddUserAskForm(ModelForm):
    """使用model创建modelform，添加手机验证"""
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """添加手机验证"""
        mobile = self.cleaned_data['mobile']
        # 电话匹配的正则
        REGEX_MOBILE = "^1[3578]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'手机号码非法', code='mobile_invalid')