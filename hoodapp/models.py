from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pic = CloudinaryField('image')

    def __str__(self):
        return self.owner.username

class Hood(models.Model):
    name = models.CharField(max_length=200)
    location =  models.CharField(max_length=200)
    img = CloudinaryField('image')
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    members = models.ManyToManyField(Profile)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name