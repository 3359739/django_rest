from django.db import models


# Create your models here.
class house(models.Model):
    name = models.CharField(max_length=100, verbose_name="房屋名称")
    address = models.CharField(max_length=100, verbose_name="房屋地址")
    phone = models.CharField(max_length=11, verbose_name="联系电话")

    class Meta:
        managed=True
        db_table = "house"

    def __str__(self):
        return self.name
class user(models.Model):
    permissions_bank=models.IntegerField(verbose_name="角色",null=True,blank=True,choices=((1,"管理员"),(2,"普通用户"),(3,"老板")),default=3)
    name = models.CharField(max_length=100, verbose_name="用户名")
    password = models.CharField(max_length=100, verbose_name="密码")
    token = models.CharField(max_length=100, verbose_name="token",null=True,blank=True)
    class Meta:
        managed=True
        db_table = "user"

    def __str__(self):
        return self.name
