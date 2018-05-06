"""MyAnimeList_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from . import views as mainViews

from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainViews.IndexPage.as_view(),name='index'),
    path('profile/',include('accounts.urls',namespace='accounts')),
    path('profile/',include('django.contrib.auth.urls')),
    path('list/',include('anime_list.urls',namespace='anime_list')),
    path('anime/',include('anime_database.urls',namespace='anime_database')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
