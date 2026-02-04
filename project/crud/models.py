from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200,null=True)
    age=models.CharField(null=True)
    email=models.EmailField(null=True)
    nessage=models.CharField(null=True)