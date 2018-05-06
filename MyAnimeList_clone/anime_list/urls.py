from django.urls import path

from anime_list.views import UserAnimeListView

app_name = 'anime_list'

urlpatterns = [
    path('<str:slug>/',UserAnimeListView.as_view(),name='user_anime_list'),
]