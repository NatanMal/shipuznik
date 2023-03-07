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
    path('my_projects', views.my_projects, name = 'my_projects'),
    path('my_profile_worker', views.my_profile_worker, name = 'my_profile_worker'),
    path('user', views.user, name = 'user'),
    path('worker', views.worker, name = 'worker'),
    path('test', views.test, name = 'test'),
    path('projects/<int:project_id>/', views.restapi_projects, name='restapi_projects'),
    path('my_quotas', views.my_quotas, name = 'my_qoutas'),
    path('readme', views.readme, name = 'readme'),
    

]
# name is the redirect
