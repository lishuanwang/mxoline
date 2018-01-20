# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.views.generic import View
from pure_pagination import PageNotAnInteger, EmptyPage, Paginator

from .models import CityDict, CourseOrg
from .forms import AddUserAskForm
from operation.models import UserAsk


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
        adduserask_from = AddUserAskForm(request.POST)
        if adduserask_from.is_valid():
            user_ask = adduserask_from.save(commit=True)
