from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField

class Hood(models.Model):
    name = models.CharField(max_length=200)
    location =  models.CharField(max_length=200)
    img = CloudinaryField('image')
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300, blank=True, null=True)
    pic = CloudinaryField('image', blank = True)
    hood = models.ForeignKey(Hood, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.owner.username