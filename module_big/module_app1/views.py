from rest_framework.authentication import BaseAuthentication
from rest_framework.response import Response
# Create your views here.
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ViewSet

from .models import user


class user_utensil(ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'


# 测试案例
class verify_class(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        if token:
            # Authentication successful
            return ("lxh", token)
        else:
            raise AuthenticationFailed("没有token")


class verify_module(ViewSet):
    authentication_classes = [verify_class]
    queryset = user.objects.all()
    serializer_class = user_utensil

    def get_all(self, req):
        print(req.user, req.auth)
        verify_success = self.serializer_class(instance=self.queryset, many=True)
        return Response(verify_success.data)


class verify_module1(ViewSet):
    authentication_classes = []
    queryset = user.objects.all()
    serializer_class = user_utensil

    def get_all(self, req):
        verify_success = self.serializer_class(instance=self.queryset, many=True)
        corresponding = Response(verify_success.data)
        return corresponding


from .authentication_moduel import *


# 登录密码
class login_password(ViewSet):
    authentication_classes = [sigin_class]
    queryset = user.objects.all()
    serializer_class = user_utensil

    def login(self, req):
        return Response({"msg": f"{cache.get("name")}"})

from django.core.cache import cache
class verify_home(ViewSet):
    authentication_classes = [verify_class1]
    queryset = user.objects.all()
    serializer_class = user_utensil

    def home(self, req):
        token=cache.get("name")
        return Response(f"首页你的token是：{token}")


from .My_api import my_api
from .my_permissions import *


# 权限
class permission_ok(my_api):
    authentication_classes = [verify_class1]
    permission_classes = [my_permissions_version1, my_permissions_version2]
    queryset = user.objects.all()
    serializer_class = user_utensil

    def get_all(self, req):
        substance = self.serializer_class(instance=self.queryset, many=True)
        return Response(substance.data)
# 认证和权限都是在寻找配配置文件
from .restriction import *
#限浏
class my_throttle_version1(my_api):
    authentication_classes = [verify_class1]
    permission_classes = [my_permissions_version1, my_permissions_version2]
    throttle_classes=[my_throttle,]
    queryset = user.objects.all()
    serializer_class = user_utensil

    def get_all(self,req):
        substance = self.serializer_class(instance=self.queryset, many=True)
        return Response(substance.data)