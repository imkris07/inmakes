from django .urls import path
from . import views
app_name='movieapp'

urlpatterns=[
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id1>/', views.update, name='update'),
    path('delete/<int:id3>/', views.delete, name='delete')

]
