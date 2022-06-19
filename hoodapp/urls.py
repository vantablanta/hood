from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.user_profile, name='profile'),
    path('update-profile/', views.update_profile, name='update-profile'),

    path('', views.home, name='home'),
    path('contact-us/', views.contact, name='contact-us'),
    path('about-us/', views.about, name='about-us'),
    path('hoods/', views.hoods, name='hoods'),
    path('join/<str:name>', views.join_hood, name='join-hood'),
    path('leave/<str:name>', views.leave_hood, name='leave'),

    path('hood/<str:name>', views.single_hood, name='hood'),
    path('add_news/<str:name>', views.add_news, name='news'),
    path('add_business/<str:name>', views.add_business, name='business'),
    path('add_amenity/<str:name>', views.add_amenity, name='amenity'),

    path('create-hood/', views.create_hood, name='create-hood'),
    path('search/', views.search, name='search')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)