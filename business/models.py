from django.db import models
from django.shortcuts import render , redirect
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save


# Create your models here.

class Neighbourhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    occupants = models.OneToOneField(User , on_delete=models.CASCADE , null= True)
    image = models.ImageField(upload_to = 'image/' , null = True)
    def __str__(self):
        return self.name

    def save_neighbourhood(self):
        self.save()    

#delete function
    @classmethod 
    def delete_neighbourhood(cls , id):
        cls.objects.filter(id=id).delete()

#search function
    @classmethod
    def search_neighbourhood(cls ,neighbourhood ):
        name = cls.objects.filter(location_name = neighbourhood)

        return name

#update function
    @classmethod
    def update(cls , id , update):
        neighbourhood=cls.objects.filter(id = id).update(neighbourhood =update)

    @classmethod
    def update(cls , id , update):
        occupants = cls.objects.filter(id=id).update(occupants = update)
    
class Profile(models.Model):
    username = models.OneToOneField(User , on_delete=models.CASCADE , null= True)
    photo= models.ImageField(upload_to = 'image/' , null = True)

    @receiver(post_save , sender = User)
    def create_user_profile(sender , instance , created , **kwargs):
        if created:
            Profile.objects.create(username = instance)
    @receiver(post_save , sender = User)
    def save_user_profile(sender , instance ,**kwargs):
        instance.profile.save()

class Business(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    description = models.TextField()
    image = models.ImageField(upload_to = 'image/' , null = True)
    def __str__(self) :
        return self.name

    #create function
    def save_business(self):
        self.save()

    @classmethod
    def search_business(cls ,business):
        business = cls.objects.filter(business_name = business)

    @classmethod
    def update(cls , id , update):
        business = cls.objects.filter(id = id).update(business = update)
