from django import db
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ex05.forms import RemovalForm

from ex05.models import Movies


def populate(request):
    movies = [
        {
            "episode_nb": 1,
            "title": "The Phantom Menace",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "1999-05-19"
        },
        {
            "episode_nb": 2,
            "title": "Attack of the Clones",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2002-05-16"
        },
        {
            "episode_nb": 3,
            "title": "Revenge of the Sith",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2005-05-19"
        },
        {
            "episode_nb": 4,
            "title": "A New Hope",
            "director": "George Lucas",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1977-05-25"
        },
        {
            "episode_nb": 5,
            "title": "The Empire Strikes Back",
            "director": "Irvin Kershner",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1980-05-17"
        },
        {
            "episode_nb": 6,
            "title": "Return of the Jedi",
            "director": "Richard Marquand",
            "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
            "release_date": "1983-05-25"
        },
        {
            "episode_nb": 7,
            "title": "The Force Awakens",
            "director": "J. J. Abrams",
            "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            "release_date": "2015-12-11"
        }
    ]

    result = []

    for movie in movies:
        try:
            Movies.objects.create(
                episode_nb=movie['episode_nb'],
                title=movie['title'],
                director=movie['director'],
                producer=movie['producer'],
                release_date=movie['release_date']
            )
            result.append('OK')
        except db.Error as e:
            result.append(e)
    return HttpResponse("<br/>".join(str(i) for i in result))


def display(request):
    try:
        movies = Movies.objects.all()
        if not len(movies):
            raise Movies.DoesNotExist
        return render(request, 'ex05/display.html', {"movies": movies})
    except Movies.DoesNotExist:
        return HttpResponse('No data available')


def remove(request):
    if request.method == 'GET':
        try:
            movies = Movies.objects.all()
            if not len(movies):
                raise Movies.DoesNotExist
        except Movies.DoesNotExist:
            return HttpResponse('No data available')
        choices = ((movie.title, movie.title) for movie in movies)
        context = {"form": RemovalForm(choices)}
        return render(request, 'ex05/remove.html', context)
    else:
        try:
            movies = Movies.objects.all()
            if not len(movies):
                raise Movies.DoesNotExist
        except Movies.DoesNotExist:
            return request.path
        choices = ((movie.title, movie.title) for movie in movies)
        data = RemovalForm(choices, request.POST)
        if data.is_valid():
            try:
                Movies.objects.get(title=data.cleaned_data['film_to_remove']).delete()
            except db.Error as e:
                print(e)
        return redirect(request.path)
