from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/<int:pk>/post_review/', views.post_review, name='post_review'),
    path('search/', views.search, name='search'),
    path('change_password/', views.change_password, name='change_password'),
    path('your-view/', views.your_view, name='your_view'),
    path('edit_movie/<int:pk>/', views.edit_movie, name='edit_movie'),
    path('delete_movie/<int:pk>/', views.delete_movie, name='delete_movie'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),

    # Add more URLs as needed
]
