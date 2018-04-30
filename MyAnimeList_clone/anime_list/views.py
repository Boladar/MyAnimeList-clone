from django.shortcuts import render
from django.views.generic import ListView, DetailView

from anime_list.models import ListElement

# Create your views here.
class AnimeList(ListView):
    model = ListElement
    template_name = 'anime_list/anime_list.html'
