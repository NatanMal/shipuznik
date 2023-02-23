from django.urls import path

from . import views

urlpatterns=[
    path('', views.registration, name = 'home'),
    path('show', views.show, name = 'show'),
    path('login', views.login, name = 'login'),
    path('profile', views.profile, name = 'profile'),
    path('search',views.search, name = 'search')
]
# name is the redirect
