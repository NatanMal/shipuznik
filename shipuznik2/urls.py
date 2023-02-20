from django.urls import path

from . import views

urlpatterns=[
    path('', views.home, name = 'home'),
    path('show', views.show, name = 'show'),
    path('login', views.login, name = 'login'),
    path('profile', views.profile, name = 'profile'),
]
# name is the redirect
