from django.urls import path

from . import views

urlpatterns=[
    path('home', views.home, name = 'home'),
    path('show', views.show, name = 'show')
]
# name is the redirect
