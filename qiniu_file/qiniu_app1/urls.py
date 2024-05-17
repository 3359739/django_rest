"""
@big_name:restful_must	
@file_name:urls	
@data:2024/5/16	
@developers:handsome_lxh
"""
from django.urls import path
from . import views
# from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'upload', views.qiniu_img_post,basename="sss")
urlpatterns=[
    path('index/<int:pk>',views.qiniu_img.as_view()),
    # path('index/',views.QiniuImgPost.as_view()),
    path('file_upload/',views.file_upload),
    path('file_download/',views.file_download),
    path('file_get/',views.file_get)
]

# urlpatterns+=router.urls

"""
views.qiniu_img.as_view()会去qiniu_img找到对应的方法而qiniu_img本身没有这个类会去其父类找到as_view()
as_view()里面实例化了qiniu_img返回一个self.dispatch
进入as_views(而as_views返回的是类内部的一个view方法)
view里面返回一个内部方法self.dispatch->(def dispatch(self, request, *args, **kwargs))
def dispatch(self, request, *args, **kwargs):
    if request.method.lower() in self.http_method_names:
        handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        这里是查找里面是否有对应的方法
    else:
        handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
        这里执行对应的方法体
总得来说是
向去qiniu_img中查找对as_view()->
as_view()->view()->dispatch()->handler()
"""