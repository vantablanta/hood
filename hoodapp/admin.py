from django.contrib import admin
from .models import Hood, Profile, News, Business, AmenityType, Amenity, Comment
# Register your models here.
admin.site.register(Profile)
admin.site.register(Hood)
admin.site.register(News)
admin.site.register(Business)
admin.site.register(Amenity)
admin.site.register(AmenityType)
admin.site.register(Comment)
