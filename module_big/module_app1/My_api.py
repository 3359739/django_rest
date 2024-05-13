"""
@big_name:restful_must	
@file_name:My_api	
@data:2024/5/13	
@developers:handsome_lxh
"""
from rest_framework.viewsets import ViewSet
class my_api(ViewSet):
    def check_permissions(self, request):
        no_premission =[]
        for permission_go in self.get_permissions():
            if permission_go.has_permission(request, self):
                return
            else:
                no_premission.append(permission_go)
        self.permission_denied(
                request,
                message=getattr(no_premission[0], 'message', None),
                code=getattr(no_premission[0], 'code', None)
        )
