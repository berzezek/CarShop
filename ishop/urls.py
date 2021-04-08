from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('carshop/', views.CarShop.as_view(), name='carshop'),
]