"""
@big_name:restful_must	
@file_name:forms	
@data:2024/5/16	
@developers:handsome_lxh
"""
from django import forms
from .models import UploadFileImg

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileImg
        fields = ['file', 'img']

class UploadFileForm_1(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()