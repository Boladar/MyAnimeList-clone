from django.db import models

# Create your models here.

class AnimeModel(models.Model):
    
    AIRING_TYPE_CHOICES = (
        ('TV', 'tv'),
        ('MOVIE','movie'),
    )

    GENRES = (
        ('ACTION','action'),
        ('DRAMA','drama'),
    )


    title = models.CharField(max_length=100)
    airing_type = models.CharField(choices=AIRING_TYPE_CHOICES)
    airing_start_date = models.DateField()
    airing_finish_date = models.DateField()
    genre = models.CharField(choices=GENRES)



class AnimeReview(models.Model):
    author = models.ForeignKey('accounts.UserProfile')

    
    