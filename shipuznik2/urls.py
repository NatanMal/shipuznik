from django.urls import path

from . import views

urlpatterns=[
    path('', views.registration, name = 'home'),
    path('show', views.show, name = 'show'),
    path('login', views.login, name = 'login'),
    path('add_project', views.add_project, name = 'add_project'),
    path('search',views.search, name = 'search'),
    path('registration',views.registration, name = 'registration'),
    path('browse',views.browse, name = 'browse'),
    path('my_profile', views.my_profile, name = 'my_profile'),
    path('my_projects', views.my_projects, name = 'my_projects')
]
# name is the redirect
