from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    fields =['desc','price']

    def __str__(self):
           return self.desc
    
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100) 
    stage = models.IntegerField()
    university = models.CharField(max_length=200)
    image = models.ImageField(upload_to='C:\LIOR\python\class\240724\frontend\student_images', null=True, blank=True)


    def __str__(self):
        return f"{self.profession} at {self.university}, stage {self.stage}"

