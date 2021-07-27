# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('genres_1', views.genres_1, name='genres_1'),
    path('final', views.final, name='final'),
    path('album', views.album, name='album'),
    path('album_variant_two', views.album_variant_two, name='album_variant_two'),
    path('end_screen', views.end_screen, name='end_screen'),
    path('indie_artists', views.indie_artists, name='indie_artists'),
    path('pop_artists', views.pop_artists, name='pop_artists'),
    path('rap_artists', views.rap_artists, name='rap_artists'),
    path('songs', views.songs, name='songs'),
    path('version', views.version, name='version'),
    path('final', views.final, name='final'),
    path('display', views.display, name='display'),

]
