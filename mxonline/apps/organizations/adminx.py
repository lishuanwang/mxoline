# -*- coding: utf-8 -*-
'''
__Author__：python
__Date__：2018/ 01/ 15/ 12/ 47 
'''
import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    list_filter = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'students', 'click_nums', 'add_time']
    list_filter = ['name', 'desc', 'students', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'students', 'click_nums']


class TeacherAdmin(object):
    list_display = ['name', 'org', 'work_years', 'work_company', 'age', 'click_nums', 'add_time']
    list_filter = ['name', 'org', 'work_years', 'work_company', 'age', 'click_nums', 'add_time']
    seach_fields = ['name', 'org', 'work_years', 'work_company', 'age', 'click_nums']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)