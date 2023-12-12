from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm


# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'Movie_list': movie
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request, "detail.html", {'movie': movie})


def add_movie(request):
    if request.method=="POST":
        name = request.POST.get('Name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = Movie(Name=name, desc=desc, year=year, img=img)
        movie.save()
    return render(request, 'add.html')


def update(request, id1):
    movie= Movie.objects.get(id=id1)

    form = MovieForm(request.POST or None, request.FILES, instance=movie)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id3):
    if request.method=='POST':
        movie1=Movie.objects.get(id=id3)
        movie1.delete()
        return redirect('/')
    return render(request, 'delete.html')
