"""
@big_name:restful_must	
@file_name:my_permissions	
@data:2024/5/13	
@developers:handsome_lxh
"""
from rest_framework.permissions import BasePermission


class my_permissions_version1(BasePermission):
    message = {
        'erro': '没有权限',
        "cole": 403
    }
    def has_permission(self, request, view):
        print(type(request.user.permissions_bank))
        if request.user.permissions_bank == 2:
            return True
        else:
            return False
class my_permissions_version2(BasePermission):
    message = {
        'erro': '没有权限',
        "cole": 403
    }
    def has_permission(self, request, view):
        print(type(request.user.permissions_bank))
        if request.user.permissions_bank == 3:
            return True
        else:
            return False
