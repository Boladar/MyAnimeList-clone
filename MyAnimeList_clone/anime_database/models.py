from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class AnimeModel(models.Model):
    
    AIRING_TYPE_CHOICES = (
        ('TV', 'tv'),
        ('MOVIE','movie'),
    )

    GENRES = (
        ('ACTION','Action'),
        ('DRAMA','Drama'),
    )


    title = models.CharField(max_length=100, primary_key = True)
    airing_type = models.CharField(choices=AIRING_TYPE_CHOICES,blank=True, null=True,max_length=10)
    airing_start_date = models.DateField(blank=True, null=True)
    airing_finish_date = models.DateField(blank=True, null=True)
    genre = MultiSelectField(choices=GENRES,blank=True, null=True)
    cover = models.ImageField(upload_to='anime_covers/',blank=True, null=True)

# TODO: 
class AnimeReview(models.Model):
    author = models.ForeignKey('accounts.UserProfile',on_delete=models.CASCADE) # propably to be changed later


    
    