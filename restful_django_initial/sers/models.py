from django.db import models

# Create your models here.
class library(models.Model):
    book_name=models.CharField(max_length=100,verbose_name="书名")
    book_author=models.CharField(max_length=100,verbose_name="作者")
    book_price=models.FloatField(verbose_name="价格")
    class Meta:
        db_table="图书馆"
        verbose_name="图书"
    def __str__(self):
        return self.book_name

