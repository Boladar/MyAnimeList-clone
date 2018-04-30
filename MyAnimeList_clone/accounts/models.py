from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

import os
import glob
from MyAnimeList_clone.settings import MEDIA_ROOT
# Create your models here.

def delete_existing_profile_picture(instance,filename):
    
    if os.path.isfile(os.path.join(MEDIA_ROOT,filename[:-3] + 'jpg')):
        path = os.path.join(MEDIA_ROOT,filename[:-3] + 'jpg')
        os.remove(path)

    if os.path.isfile(os.path.join(MEDIA_ROOT,filename[:-3] + 'png')):
        path = os.path.join(MEDIA_ROOT,filename[:-3] + 'png')
        os.remove(path)
    
    
def user_direcotry_path(instance,filename):
    file_extension = filename[-3:]
    name = instance.user.username

    file_path = 'profile_pictures/' + name + '.' + file_extension

    delete_existing_profile_picture(instance,file_path)
    return file_path

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=60, primary_key=True)
    profile_picture = models.ImageField(upload_to=user_direcotry_path,blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('accounts:profile_detail',args =[self.username])