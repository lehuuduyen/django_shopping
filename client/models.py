from django.db import models
from django.contrib.auth.models import User
import re
from django.utils.html import format_html
# Create your models here.
ORDER_STATUS = ((0, 'Close'), (1, 'Open'))


def no_accent_vietnamese(s):
    s = s.lower()
    s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub('[íìỉĩị]', 'i', s)
    s = re.sub('[úùủũụưứừửữự]', 'u', s)
    s = re.sub('[ýỳỷỹỵ]', 'y', s)
    s = re.sub('đ', 'd', s)
    return s

class Slide(models.Model):

    title  =    models.TextField(null=True)
    image   =   models.ImageField()
    date    =   models.DateTimeField(auto_now_add =True)
    status  =   models.PositiveSmallIntegerField(choices=ORDER_STATUS)



class New(models.Model):

    title           =    models.CharField(max_length=255)
    content         =    models.TextField(null=True)
    image           =     models.ImageField(null=True)
    content_fast    =     models.CharField(max_length=255,null=True)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    status          = models.PositiveSmallIntegerField(choices=ORDER_STATUS)
    created_by      = models.ForeignKey(User, on_delete=models.PROTECT)
       
    def __str__(self):
        self.path = self.title.replace(' ','-')
        return no_accent_vietnamese(self.path)
    
  

class Comment(models.Model):
    name            = models.CharField(max_length=100,default="Người vô danh")
    content         = models.TextField()
    sub_comment     = models.IntegerField(default=0)
    image           = models.ImageField(default="default.jpeg")
    created_at      = models.DateTimeField(auto_now_add=True)
    new_id          = models.ForeignKey(New,on_delete=models.CASCADE, related_name='comments')



class Category(models.Model):
    name            = models.CharField(max_length=365)
    path_name       = models.CharField(max_length=365,null=True)
    description     = models.TextField()
    sub_category    = models.IntegerField(default=0)
    image           = models.ImageField(default="default.jpeg")
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    status          = models.PositiveSmallIntegerField(choices=ORDER_STATUS,default=1)
    def save(self, *args, **kwargs):
        self.path_name = no_accent_vietnamese(self.name).replace(' ','-')
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name 

class Product(models.Model):
    name            = models.CharField(max_length=365)
    description     = models.TextField()
    category_id     = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    
 
class Imgae(models.Model):
    image           = models.ImageField(default="default.jpeg")
    product_id     = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='images')
    status          = models.PositiveSmallIntegerField(choices=ORDER_STATUS)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
 
