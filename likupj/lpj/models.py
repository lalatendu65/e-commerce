
from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=70)
    gender=models.CharField(max_length=1)
    location=models.CharField(max_length=100)
    Rollno=models.IntegerField()

class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50, default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=500) 
    product_date=models.DateField()
    image=models.ImageField(upload_to='static/img',default="")

    def __str__(self):
        
        return self.product_name



