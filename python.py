from django.db import models

# Create your models here.

class Member(models.Model):
    First_Name = models.CharField(max_length=25)
    Last_Name = models.CharField(max_length=25)
    date_of_birth = models.DateField(null=True)
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)