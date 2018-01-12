from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class CourseDetail(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"课程名称")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(max_length=10, verbose_name=u"难度", \
                             choices=(("low", u"低级"), ("middle",u"中级"),("high", u"高级")))
    number = models.IntegerField(max_length=10, verbose_name=u"学习人数")
    time = models.CharField(max_length=5, )