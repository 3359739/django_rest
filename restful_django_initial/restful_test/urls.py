from django.urls import path
from django.conf.urls import include
from .views import resrful_test,resrful_test_version2
"""
这两种是django代码调用视图的两种方式
FBV:就是直接调用函数
CBV：而且cbv是类，所以要实例化，然后调用as_view方法其实本质上也是fbv
"""
urlpatterns=[
    path("restful_initial/",resrful_test.as_view(),name="restful_initial"),
    #本质其实向到视图找到resrful_test类然后调用类里面的as_view方法
    # """
    # 为什么是fbv也是他也是通过一步一步找到然后进行调用
    # 例如：resrful_test.as_view()
    # 然后去视图上找到resrful_test(view)是继承了view
    # view调用as_view()
    # 所有本质上还是调用函数执行
    # """

    path("restful_initial_version/", resrful_test_version2.as_view(), name="restful_initial"),
]

