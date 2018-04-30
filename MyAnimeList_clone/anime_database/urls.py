from django.urls import path
from anime_database import views

app_name = 'anime_database'

urlpatterns = [
    path('',views.AnimeList.as_view(),name='anime_list'),
    path('detail/<str:slug>',views.AnimeDetail.as_view(),name='anime_detail'),
]