from . import views
from django.urls import path


urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),

    path('', views.home, name='home'),
    path('contact-us/', views.contact, name='contact-us'),
    path('about-us/', views.about, name='about-us'),
    path('hoods/', views.hoods, name='hoods'),
    path('create-hood/', views.create_hood, name='create-hood')
]