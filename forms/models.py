from django.db import models

# Create your models here.

class FakeUser(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    password = models.CharField(max_length=500)
    age = models.IntegerField()
