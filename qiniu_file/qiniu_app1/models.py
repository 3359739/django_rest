from django.db import models

# Create your models here.
class UploadFileImg(models.Model):
    file =models.FileField(upload_to='files/')
    img =models.ImageField(upload_to='imgs/')
    remark = models.CharField(max_length=100)
    class Meta:
       db_table = 'img'
