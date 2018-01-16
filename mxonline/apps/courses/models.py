# coding=utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from organizations.models import CourseOrg


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"课程名称")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(max_length=6, verbose_name=u"难度", \
                              choices=(("low", u"低级"), ("middle", u"中级"), ("high", u"高级")))
    # course_type = models.CharField(max_length=20, verbose_name=u"学习类别")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时长（以分钟计算）")
    click = models.IntegerField(default=0, verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"上传时间")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name=u"缩略图")

    class Meta:
        verbose_name = u"课程信息表"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name


class Lession(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"所属课程")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长")
    name = models.CharField(max_length=50, verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lession = models.ForeignKey(Lession, verbose_name=u"所属章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名称")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长")
    url = models.URLField(max_length=100, verbose_name=u"视频地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"所属课程")
    name = models.CharField(max_length=10, verbose_name=u"资源名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源下载", max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"资源"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
