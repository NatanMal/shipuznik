from django.urls import path

from . import views

urlpatterns=[
    path('', views.registration, name = 'home'),
    path('show', views.show, name = 'show'),
    path('login', views.login, name = 'login'),
    path('profile', views.profile, name = 'profile'),
    path('search',views.search, name = 'search'),
    path('registration',views.registration, name = 'registration'),
    path('browse',views.browse, name = 'browse')
]
# name is the redirect
