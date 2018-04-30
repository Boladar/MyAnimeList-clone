from django.shortcuts import render
from django.views.generic import ListView,DetailView

from anime_database.models import AnimeModel
# Create your views here.

class AnimeList(ListView):
    
    template_name = 'anime_database/anime_list.html'
    model = AnimeModel
    paginate_by = 5

class AnimeDetail(DetailView):
    model = AnimeModel
    slug_field = 'title'
    template_name='anime_database/anime_detail.html'