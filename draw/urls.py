# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('genres_1', views.genres_1, name='genres_1'),
    path('final', views.final, name='final'),
    path('display', views.display, name='display'),

]
