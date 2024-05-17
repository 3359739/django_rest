"""
@big_name:restful_must	
@file_name:request大概	
@data:2024/5/17	
@developers:handsome_lxh
"""


class HttpRequest(object):
    def __init__(self):
        self.ww=123
        # pass

    def v1(self):
        print("v1")

    def v2(self):
        print("v2")


class Request(object):
    def __init__(self, req, xx):
        self._request = req
        self.xx = xx

    def __getattr__(self, attr):
        # print(attr)
        try:
            return getattr(self._request, attr)
        except AttributeError:
            return self.__getattribute__(attr)

#
# request = HttpRequest()
# request.v1()
# request.v2()
# request = Request(request, 111)
# request.v1()
# request.v2()
#
# # print(request.ww)

class fun(object):
    def __init__(self):
        self.name="handsome_lxh"

class fun_version(object):
    def __init__(self):
        pass
        def __getattr__(self, item):
        print("ss1",item)
        return 123456
    def __getattribute__(self, item):
        print("ss",item)
substance=fun_version()
# print(substance.name)
# print(substance)
print(getattr(substance, "weixing", "123456"))
"""
getattr(类,属性名,默认值)获取
setattr(类,属性名,属性值)设置
hasattr(类,属性名)判断
delattr(类,属性名)删除
__getattribute__:在获取属性时调用
__getattr__:调用不存在的返值触发
"""