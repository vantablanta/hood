from django.test import TestCase
from django.test import TestCase
from .models import  Hood, Profile, Business
from django.contrib.auth.models import User



class HoodTest(TestCase):
    def setUp(self):
        self.new_user = User(username='Michelle')
        self.new_user.save()

        self.new_hood = Hood(name='Test Hood', admin= self.new_user, 
        location='hood location')
        self.new_hood.save()

        self.new_profile = Profile(bio='test bio', owner=self.new_user, 
        hood=self.new_hood)
        self.new_profile.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_hood, Hood))

    def test_save_method(self):
        self.new_hood.create_neighborhood()
        hood = Hood.objects.all()
        self.assertTrue(len(hood) > 0 )

    def test_delete_method(self):
        self.new_hood.save()
        self.new_hood.delete_neighborhood()
        hood = Hood.objects.all()
        self.assertTrue(len(hood) == 0 )


class BusinessTest(TestCase):
    def setUp(self):
        self.new_user = User(username='Michelle')
        self.new_user.save()

        self.new_hood = Hood(name='Test Hood', admin= self.new_user, 
        location='hood location')
        self.new_hood.save()

        self.new_profile = Profile(bio='test bio', owner=self.new_user, 
        hood=self.new_hood)
        self.new_profile.save()

        self.new_business = Business(name='Test Hood', owner= self.new_profile, 
        location='hood location', contact='0723217050', hood=self.new_hood)
        self.new_business.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business, Business))

    def test_save_method(self):
        self.new_business.create_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0 )

    def test_delete_method(self):
        self.new_business.save()
        self.new_business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business) == 0 )