from django.db import models
class Actor(models.Model):
    name=models.CharField(max_length=70)
    gender=models.CharField(max_length=1)
    location=models.CharField(max_length=100)
    movies=models.IntegerField()

# Create your models here.
