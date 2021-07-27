# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def album(request):
    return render(request, 'draw/album.html')

def album_variant_two(request):
    return render(request, 'draw/album_variant_two.html')

def end_screen(request):
    return render(request, 'draw/end_screen.html')

def indie_artists(request):
    return render(request, 'draw/indie_artists.html')

def pop_artists(request):
    return render(request, 'draw/pop_artists.html')

def rap_artists(request):
    return render(request, 'draw/rap_artists.html')

def songs(request):
    return render(request, 'draw/songs.html')

def version(request):
    return render(request, 'draw/version.html')

def genres_1(request):
    return render(request, 'draw/genres_1.html')

def final(request):
    return render(request, 'draw/final.html')

def display(request):
    return render(request, 'draw/display.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })
