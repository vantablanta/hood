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

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, hood_id):
        return cls.objects.filter(id=hood_id)

class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300, blank=True, null=True)
    pic = CloudinaryField('image', blank = True)
    hood = models.ForeignKey(Hood, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.owner.username

class News(models.Model):
    poster = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=True, null=True)
    body = models.TextField()
    hood = models.ForeignKey(Hood, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title

    class Meta():
        ordering = ['-created']

class Business(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=300)
    contact = models.CharField(max_length=300, blank=True, null=True)
    hood = models.ForeignKey(Hood, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()


class AmenityType(models.Model):
    name = models.CharField(max_length=300)
    listed_by = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

    def __str__(self) :
            return self.name

class Amenity(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, blank=True, null=True)
    type = models.ForeignKey(AmenityType, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=300)
    phone = models.CharField(max_length=300, blank=True, null=True)
    email = models.CharField(max_length=300, blank=True, null=True)
    hood = models.ForeignKey(Hood, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name

class Comment(models.Model):
    poster = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField()
    hood = models.ForeignKey(Hood, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) :
           return f'{self.poster}"s comment'

class Contact(models.Model):
    name = models.CharField(max_length=300)
    phone = models.TextField()
    email = models.CharField(max_length=300)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
           return f"{self.name}'s message"



