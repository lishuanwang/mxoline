# coding=utf-8
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course


class UserAsk(models.Model):
    name = models.CharField(verbose_name=u"名字", max_length=20, null=False, blank=False)
    mobile = models.CharField(verbose_name=u"电话", max_length=11, null=False, blank=False)
    course_name = models.CharField(verbose_name=u"咨询课程", max_length=50)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"用户咨询表"
        verbose_name_plural = verbose_name


class CourseComment(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    comment = models.CharField(verbose_name=u"评论", max_length=200)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"用户评论表"
        verbose_name_plural= verbose_name


class UserFaverite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.CharField(default=0, verbose_name=u"用户id")
    fav_type = models.CharField(default=1, choices=((1, "课程"), (2, "课程机构"), (3, "讲师")),\
                                verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户收藏表"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u"接收用户")
    message = models.CharField(max_length=300, verbose_name=u"信息")
    has_read = models.BooleanField(default=False, verbose_name=u"是否已经读过")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户信息表"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户收藏课程表"
        verbose_name_plural = verbose_name







