from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Course(models.Model):
    CAT = ((1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced'))
    title = models.CharField(max_length=100,verbose_name='Course Name')
    description = models.CharField(max_length=500)
    cate=models.IntegerField(verbose_name='Category',choices=CAT)
    price = models.FloatField()
    is_active=models.BooleanField(default=True,verbose_name='Avilable')
    image = models.ImageField(upload_to='image')
    def __str__(self):
        return self.title

class enroll(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    cid=models.ForeignKey(Course,on_delete=models.CASCADE,db_column="cid")

class Order(models.Model):
    order_id=models.CharField(max_length=50)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(Course,on_delete=models.CASCADE,db_column="pid")

class Enroll1(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    cid=models.ForeignKey(Course,on_delete=models.CASCADE,db_column="cid")