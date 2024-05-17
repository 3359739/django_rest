from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView

from .forms import UploadFileForm
# Create your views here.
from .models import UploadFileImg
from rest_framework.response import Response

from rest_framework.parsers import MultiPartParser
from .models import UploadFileImg
from rest_framework import serializers
class qiniu_img(APIView):
    parser_classes = [MultiPartParser]
    def get(self,req,pk):
        img_qiniu=UploadFileImg.objects.get(pk=pk)
        print(dir(img_qiniu))
        print(img_qiniu.file.url)
        return render(req,"imgs.html",{"uploadFileImg":img_qiniu})
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFileImg
        fields = '__all__'
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from .forms import UploadFileForm


def file_upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        uploaded_file1 = request.FILES['img']
        uploaded_file2 = request.POST['remark']
        wei=UploadFileImg.objects.create(file=uploaded_file,img=uploaded_file1,remark=uploaded_file2)
        wei.save()
        return HttpResponse("上传成功")
    else:
        form = UploadFileForm()
    return render(request, 'file_upload.html')

def file_download(request):
    img_qiniu = UploadFileImg.objects.get(pk=7)
    return render(request, "imgs.html", {"uploadFileImg": img_qiniu})
from . import models
def file_get(req):
    img_qiniu = models.UploadFileImg.objects.raw("select * from img ")
    print(img_qiniu[0].file)
    return  HttpResponse("123456")
