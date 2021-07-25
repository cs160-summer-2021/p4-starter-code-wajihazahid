# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def genres_1(request):
    return render(request, 'draw/genres_1.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })


