#员工信息管理的视图文件
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.
from myadmin.models import User

def index(request,pIndex=1):
    '''浏览信息'''
    umod = User.objects
    ulist = umod.filter(status__lt=9)

    #执行分页处理
    pIndex = int(pIndex)
    page = Paginator(ulist,5) #以每页5条数据进行
    maxpages = page.num_pages #最大页数
    #判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) #获取当前页数据
    plist = page.page_range #获取页码列表信息


    
    context = {"userlist":list2,"plist":plist,"pIndex":pIndex,"maxpages":maxpages}
    return render(request,"myadmin/user/index.html",context)

def add(request):
    '''加载信息添加表单'''
    pass

def insert(request):
    '''执行信息添加'''
    pass

def delete(request,uid=0):
    '''执行信息删除'''
    pass

def edit(request,uid=0):
    '''加载信息编辑表单'''
    pass

def update(request,uid=0):
    '''执行信息更新'''
    pass