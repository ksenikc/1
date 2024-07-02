from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    full_name = models.CharField(max_length=200)
    # city = models.CharField(max_length=100)
    
class Statement(models.Model):
    # adress = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
