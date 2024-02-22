from django.urls import path
from . import views

app_name='Ecommerce_app'

urlpatterns=[
    path('', views.allprodcat, name='allprodcat'),
    path('<slug:c_slug>/', views.allprodcat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetail, name='prodcatdetail'),

]
