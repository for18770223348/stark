from django.db import models

# Create your models here.


class Usertype(models.Model):
    '''
    职位
    '''
    title=models.CharField(max_length=32)

class Userinfo(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    header_color=models.CharField(max_length=32)

    type=models.ForeignKey(to=Usertype,null=True,blank=True)