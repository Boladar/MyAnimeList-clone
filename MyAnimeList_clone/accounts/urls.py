from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

app_name ='accounts'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('register/',views.SignUp,name='register'),
    path('<str:slug>/',views.ProfileDetailView.as_view(),name='profile_detail'),
    path('<str:slug>/update/',views.ProfileUpdateView.as_view(),name='profile_update'),
]