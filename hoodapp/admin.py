from django.contrib import admin
from .models import Hood, Profile, News
# Register your models here.
admin.site.register(Profile)
admin.site.register(Hood)
admin.site.register(News)
