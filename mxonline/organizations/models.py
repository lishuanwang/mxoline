# coding=utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市名称")
    desc = models.CharField(max_length=300, verbose_name=u"描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"城市列表"
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    city = models.ForeignKey(CityDict, verbose_name=u"所属城市")
    name = models.CharField(max_length=20, verbose_name=u"机构名称")
    desc = models.TextField(verbose_name=u"机构描述")
    image = models.ImageField(verbose_name=u"缩略图", upload_to="courseorg/%Y%m",\
                              default="courseorg/default.png", max_length=100)
    students = models.IntegerField(verbose_name=u"学生数量", default=0)
    fav_nums = models.IntegerField(verbose_name=u"收藏人数", default=0)
    address = models.CharField(verbose_name=u"机构地址", max_length=100)
    coursenum = models.IntegerField(verbose_name=u"课程数量", default=0)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)
    click_nums = models.IntegerField(verbose_name=u"点击数量", default=0)

    class Meta:
        verbose_name = u"课程机构表"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")
    name = models.CharField(verbose_name=u"教师姓名", max_length=50)
    work_years = models.IntegerField(verbose_name=u"工作年限", default=0)
    work_company = models.CharField(verbose_name=u"就职公司", max_length=50)
    work_position = models.CharField(verbose_name=u"工作职位", max_length=50)
    point = models.CharField(verbose_name=u"教学特点", max_length=20)
    age = models.IntegerField(verbose_name=u"年龄", default=18)
    click_nums = models.IntegerField(verbose_name=u"点击数", default=0)
    fav_nums = models.IntegerField(verbose_name=u"收藏数量", default=0)
    image = models.ImageField(verbose_name=u"缩略图", upload_to="teacher/%Y/$m", default="", max_length=100)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"教师表"
        verbose_name_plural = verbose_name


