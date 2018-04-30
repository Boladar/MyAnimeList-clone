from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
# Create your models here.

def user_direcotry_path(instance,filename):
    file_extension = filename[-3:]
    name = instance.user.username
    return 'profile_pictures/' + name + '.' +  file_extension

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=60, primary_key=True)
    profile_picture = models.ImageField(upload_to=user_direcotry_path,blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('accounts:profile_detail',args =[self.username])