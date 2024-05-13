"""
URL configuration for module_big project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import  include
from module_app1.views import verify_module,verify_module1,login_password,verify_home,permission_ok,my_throttle_version1
from rest_framework import  routers
# router=routers.SimpleRouter()
# router.register("module_verify",house,basename="house_verify")
urlpatterns = [
   path("verify/",verify_module.as_view({"get":"get_all"})),
   path("verify1/",verify_module1.as_view({"get":"get_all"})),
   # 认证
   path("verify2/",login_password.as_view({"post":"login"})),
   path("verify3/",verify_home.as_view({"get":"home"})),

   #权限
   path("verify4/",permission_ok.as_view({"get":"get_all"})),
   path("verify5/",my_throttle_version1.as_view({"get":"get_all"}))

]
# urlpatterns+=router.urls