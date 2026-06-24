

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    #path("admin/", admin.site.urls),
    path("",include("web.urls")), #默认访问前台大堂点餐
    path("myadmin/",include("myadmin.urls")),#后台管理
    path("mobile/",include("mobile.urls")),  #移动端

]
