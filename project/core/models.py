from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200,null=True)
    age=models.IntegerField()
    phone=models.IntegerField()
    nessage=models.TextField()