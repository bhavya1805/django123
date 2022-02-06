from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='book/pdf')
    cover=models.ImageField(upload_to='book/cover',null=True,blank=True)


class CustomUser(AbstractUser):
    email=models.CharField(max_length=100)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)

class order(models.Model):
    name=models.CharField(max_length=100)
    phno=models.IntegerField()
    location=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
