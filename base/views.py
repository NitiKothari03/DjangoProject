from django.shortcuts import render
from .models import Movie

rooms = [
    {'id' : 1, 'name' : 'Niti'},
    {'id' : 2, 'name' : 'ABC'},
    {'id' : 3, 'name' : 'XYZ'},
{'id' : 4, 'name' : 'PQR'}
]

def home(request):
    searchTerm = request.GET.get('searchMovie')
    movies = Movie.objects.all()
    return render(request, 'home.html', {'rooms' : rooms, 'movies' : movies, 'search' : searchTerm})

def room(request):
    return render(request, 'room.html', {'rooms' : rooms})
