"""
@big_name:restful_must	
@file_name:urls	
@data:2024/5/10	
@developers:handsome_lxh
"""

from django.urls import path

from . import views
from rest_framework import  routers
# 直接帮我们写好了内容
router = routers.SimpleRouter()
router.register("test_day1",views.test_day1,basename="test_day1")
router.register("test_day1/<int:pk>",views.test_day1,basename="test_day2")
# "相当↓"
# path("last_views45/", views.test_day1.as_view({"get": "list", "post": "create"})),
# path("last_views45/<int:pk>/",
#      views.test_day1.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}))
urlpatterns = [
    # 基础版
    path("restful_rers/", views.rers.as_view()),
    path("restful_rers/<int:id>", views.single_operation.as_view()),
    # 进阶版
    path("automaic/", views.automatic_sers.as_view()),  # 描述实例化器serializers.ModelSerializer
    path("sers_gener/", views.sers_gener.as_view()),  # 描述GenericAPIView
    path("sers_gener/<int:pk>", views.sers_gener_version2.as_view()),
    # mixin混入
    path("mixin_initital/", views.sers_gener_version3.as_view()),  # 基础版
    path("mixin_initital/<int:pk>", views.sers_gener_version4.as_view()),  # 基础版
    path("mixin_initital_upgrade/", views.sers_gener_version5.as_view()),
    path("mixin_initital_upgrade/<int:pk>", views.sers_gener_version6.as_view()),

    # 视图最强版
    # 简单测试用例
    path("sers_gener_upgrade/", views.automaic_utensil_viewset.as_view({"get": "get_all", "post": "post_create"})),
    path("sers_gener_upgrade/<int:pk>",
         views.automaic_utensil_viewset.as_view({"get": "get_one", "put": "put_update", "delete": "delete_delete"})),
    # 增删改查
    # 继承了ViewSet对路由的重新分发和mixin的内容直接把mixin里面的增删改查重写
    path("last_views/", views.automaic_utensil_viewset2.as_view({"get": "list", "post": "create"})),
    path("last_views/<int:pk>/",
         views.automaic_utensil_viewset2.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path("last_views2/", views.automaic_utensil_viewset3.as_view({"get": "list", "post": "create"})),
    path("last_views2/<int:pk>/",
         views.automaic_utensil_viewset3.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    # path("last_views45/", views.test_day1.as_view({"get": "list", "post": "create"})),
    # path("last_views45/<int:pk>/",
    #      views.test_day1.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}))

]
# 路由分发restful简化路由分配
urlpatterns += router.urls