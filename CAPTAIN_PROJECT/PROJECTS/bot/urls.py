from bot import views
from django.urls import path 

urlpatterns = [
    path('', views.index, name='index'),
    path('captain/', views.base, name='base'),
    path('runbot/', views.startprogram, name='startname'),
    path('logs/', views.showlog, name='showlog'),
]
