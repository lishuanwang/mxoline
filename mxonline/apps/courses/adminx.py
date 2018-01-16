# -*- coding: utf-8 -*-
'''
__Author__：python
__Date__：2018/ 01/ 15/ 16/ 13 
'''
import xadmin

from .models import Course, Lession, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'students', 'fav_nums', 'click', 'add_time']
    list_filter = ['name', 'desc', 'students', 'fav_nums', 'click', 'add_time']
    search_field = ['name', 'desc', 'students', 'fav_nums', 'click']


class LessionAdmin(object):
    list_display = ['name', 'course', 'add_time']
    list_filter = ['name', 'course__name', 'add_time']
    search_field = ['name', 'course' ]


class VideoAdmin(object):
    list_display = ['name', 'lession', 'add_time']
    list_filter = ['name', 'lession', 'add_time']
    search_field = ['name', 'lession']


class CourseResourceAdmin(object):
    list_display = ['name', 'course', 'add_time']
    list_filter = ['name', 'course', 'add_time']
    search_field = ['name', 'course']

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lession, LessionAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
