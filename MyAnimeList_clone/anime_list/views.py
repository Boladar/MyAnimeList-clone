from django.shortcuts import render
from django.views.generic import ListView, DetailView

from anime_list.models import UserAnimeList

# Create your views here.
class UserAnimeListView(DetailView):
    model = UserAnimeList
    template_name = 'anime_list/anime_list.html'
    slug_field = 'owner'
