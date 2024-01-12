from . import views
from django.urls import path


urlpatterns= [
    path('registeration', views.registeration, name='registration'),
    path('login', views.login, name='login'),
    path('logout',views.logout, name='logout')
]
