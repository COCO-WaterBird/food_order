from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import User
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

#后台管理首页
def index(request):
    return render(request, "myadmin/index/index.html")


#管理员登录表单
def login(request):
    return render(request, "myadmin/index/login.html")

#执行管理员登录
def dologin(request):
    '''执行会员登录'''
    try:
        #根据登录账号获取登录者信息
        user = User.objects.get(username=request.POST['username'])
        #判断当前用户是否是管理员
        if user.status == 6:
            #判断登录密码是否相同
            import hashlib
            md5 = hashlib.md5()
            s = request.POST['password'] + user.password_salt #从表单中获取密码并添加干扰值
            md5.update(s.encode('utf-8')) #将要产生的md5子串放进去
            if user.password_hash == md5.hexdigest(): #获取md5值
                print("登录成功")
                #将当前登录成功的用户信息以adminuser为key写入到session中
                # request.session['adminuser'] = user.toDict() #
                request.session['adminuser'] = {
                    "id": user.id,
                    "username": user.username,
                    "nickname": user.nickname,
                    "status": user.status,
                }
                #重定向到后台管理首页
                return redirect(reverse("myadmin_index"))
            else:
                context = {"info": "登录密码错误！"}
        else:
            context = {"info": "无效的登录账户！"}
            
            
    except Exception as err:
        print(err)
        context = {"info": "登录账号不存在！"}
    return render(request, "myadmin/index/login.html", context)

    
#执行管理员退出
def logout(request):
    del request.session['adminuser']
    return redirect(reverse("myadmin_logins"))