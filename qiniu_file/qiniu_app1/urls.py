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
    path('file_download/',views.file_download)
]

# urlpatterns+=router.urls