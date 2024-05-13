from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView

# Create your views here.
from django.views import View
# cbv
class resrful_test(View):
    def __init__(self,**args):
        super().__init__()
    def get(self,request):
        # print(dir(request))
        print(request.body)

        return HttpResponse("我是get请求。。。。。")
    def post(self,request):
        return HttpResponse("我是post请求。。。。。")
    def put(self,request):
        return HttpResponse("我是put请求。。。。。")
# restful
class resrful_test_version2(APIView):
    def get(self,request):
        print(f"我是get-》{request.query_params}")#get请求获取伟query_params
        return HttpResponse("我是get请求。。。。。")
    def post(self,request):
        print(f"我是post-》{request.data}")# post请求获取伟data
        return HttpResponse("我是post请求。。。。。")
    def put(self,request):
        return HttpResponse("我是put请求。。。。。")
