# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from pure_pagination import PageNotAnInteger, EmptyPage, Paginator

from .models import CityDict, CourseOrg, Teacher
from .forms import AddUserAskForm
from operation.models import UserFaverite


class OrgListView(View):
    def get(self, request):
        """机构列表页面GET返回数据"""
        all_city = CityDict.objects.all()
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by('-click_nums')[:3]
        # 按照城市来筛选
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=city_id)
        # 按照机构类型来筛选
        org_type = request.GET.get('ct', '')
        if org_type:
            all_orgs = all_orgs.filter(type=org_type)
        # 统计符合以上所有条件的对象个数
        orgs_count = all_orgs.count()


        # 分类排序
        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_orgs = all_orgs.order_by('-students')
        elif sort == 'courses':
            all_orgs = all_orgs.order_by('-coursenum')

        # 分页设置
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        orgs_page = Paginator(all_orgs, 2, request=request)
        orgs = orgs_page.page(page)
        # 上下文
        context = {
            'cities': all_city,
            'orgs': orgs,
            'orgs_count': orgs_count,
            'city_id': city_id,
            'org_type': org_type,
            'sort': sort,
            'hot_orgs': hot_orgs,
        }
        return render(request, 'org-list.html', context)


class AddUserAskView(View):
    """增加列表页用户咨询表单"""
    def post(self, request):
        # post请求处理函数
        adduserask_from = AddUserAskForm(request.POST)
        if adduserask_from.is_valid():
            user_ask = adduserask_from.save(commit=True)
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "msg": "提交失败"}', content_type='application/json')


class OrgHomeView(View):
    """机构首页类创建"""
    def get(self, request, org_id):
        current_page = 'home'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()[:3]
        teachers = course_org.teacher_set.all()[:1]
        has_fav = False
        if request.user.is_authenticated():
            if UserFaverite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        context = {
            'courses': all_courses,
            'teachers': teachers,
            'course_org': course_org,
            'current': current_page,
            'hav_fav': has_fav,
        }
        return render(request, 'org-detail-homepage.html', context)


class OrgCourseView(View):
    """机构课程页面"""
    def get(self, request, org_id):
        current_page = 'course'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()
        has_fav = False
        if request.user.is_authenticated():
            if UserFaverite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        context={
            'courses': all_courses,
            'course_org': course_org,
            'current': current_page,
            'hav_fav': has_fav,
        }
        return render(request, 'org-detail-course.html', context)


class OrgDescView(View):
    """机构描述页面"""
    def get(self, request, org_id):
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFaverite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        context = {
            'course_org': course_org,
            'current': current_page,
            'hav_fav': has_fav,
        }
        return render(request, 'org-detail-desc.html', context)


class OrgTeacherView(View):
    """机构老师页面"""
    def get(self, request, org_id):
        current_page = 'teacher'
        course_org = CourseOrg.objects.get(id=int(org_id))
        teachers = course_org.teacher_set.all()
        has_fav = False
        if request.user.is_authenticated():
            if UserFaverite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        context ={
            'current': current_page,
            'teachers': teachers,
            'course_org': course_org,
            'hav_fav': has_fav,
        }
        return render(request, 'org-detail-teachers.html', context)


class AddFavView(View):
    """用户收藏模块"""
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)
        # 判断用户登陆状态，返回json
        if not request.user.is_authenticated:
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        # 用户登陆的话，查询他现有的收藏状态
        exist_records = UserFaverite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:
            # 如果记录存在，则表示用户需要删除收藏
            exist_records.delete()
            return HttpResponse('{"status":"success", "msg":"收藏"}', content_type='application/json')
        else:
            user_fav = UserFaverite()
            if int(fav_id)>0 and int(fav_type)>0 :
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status": "fail", "msg": "收藏出错"}', content_type='application/json')




































