# -*- coding:utf-8 -*-  
""" 
@author:python 
@file: forms.py 
@time: 2018/01/20/22/49 
"""

from django.forms.models import ModelForm

from operation.models import UserAsk


class AddUserAskForm(ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']