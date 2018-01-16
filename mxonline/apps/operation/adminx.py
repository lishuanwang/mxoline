# -*- coding:utf-8 -*-
""" 
@author:python 
@file: adminx.py 
@time: 2018/01/15/21/33 
"""

import xadmin

from .models import UserAsk, CourseComment, UserFaverite, UserMessage


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']


class CourseCommentAdmin(object):
    list_display = ['user', 'course', 'comment', 'add_time']
    list_filter = ['user', 'course', 'comment', 'add_time']
    search_fields = ['user', 'course', 'comment']


class UserFaveriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    list_filter = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFaverite, UserFaveriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)


