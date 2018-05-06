from django.contrib import admin

from anime_list.models import ListElement,UserAnimeList
# Register your models here.
admin.site.register(ListElement)
admin.site.register(UserAnimeList)