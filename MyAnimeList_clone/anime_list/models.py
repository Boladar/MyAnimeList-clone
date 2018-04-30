from django.db import models

from anime_database.models import AnimeModel
# Create your models here.

class ListElement(models.Model):
    
    anime = models.OneToOneField(AnimeModel,related_name='anime_user_list',on_delete=models.PROTECT)
    score = models.IntegerField(blank=True, null=True)
    progress = models.IntegerField(default=0) # choices set in form

    def __str__(self):
        return self.anime.title