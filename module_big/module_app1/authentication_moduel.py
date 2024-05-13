"""
@big_name:restful_must	
@file_name:authentication_moduel	
@data:2024/5/12	
@developers:handsome_lxh
"""
from uuid import uuid4
from .models import user
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.core.cache import cache
class sigin_class(BaseAuthentication):
    def authenticate(self, request):
        username=request.data.get("name")
        password=request.data.get("password")
        substance=user.objects.filter(name=username,password=password).first()
        if substance:
            substance.token=uuid4()
            cache.set(substance,substance.token)
            substance.save()
            return (substance,username)
        else:
            raise AuthenticationFailed("用户名或密码错误")
class verify_class1(BaseAuthentication):
    def authenticate(self, request):
        token=cache.get("name")
        substance=user.objects.filter(token=token).first()
        if substance:
            return (substance,token)
        else:
            raise AuthenticationFailed("用户认证失败")