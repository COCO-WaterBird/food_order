#执行是否登录判断
from django.shortcuts import redirect
from django.urls import reverse
import re



class ShopMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("ShopMiddleware")

    def __call__(self, request):
        path = request.path
        print("url:", path)

        #判断管理后台是否登录
        urllist = ['/myadmin/login/','/myadmin/logout/','/myadmin/dologin/','/myadmin/verify','/myadmin/verify/','/myadmin/login','/myadmin/logout','/myadmin/dologin']
        #判断当前请求url地址是否以myadmin开头,并且不在urllist中,才做判断
        if re.match(r'^/myadmin', path) and (path not in urllist):
            #判断是否已经登录(在session中是否有adminuser信息)
            if 'adminuser' not in request.session:
            #重定向到登录页
                return redirect(reverse("myadmin_login"))

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response