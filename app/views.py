from itertools import chain
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from .models import Movie, Category, Serie, Episode
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieSerializer
from itertools import chain

class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

def index(request):
    categories = Category.objects.order_by('name')
    movies_ajnabi = Movie.objects.filter(category=3)[:4]
    movies_arab = Movie.objects.filter(category=4)[:4]
    movies_hindi = Movie.objects.filter(category=6)[:4]
    movies_asian = Movie.objects.filter(category=5)[:4]
    series = Serie.objects.filter(is_tvshow=False)
    context={
        'movies_ajnabi':movies_ajnabi,
        'movies_arab':movies_arab,
        'movies_hindi':movies_hindi,
        'movies_asian':movies_asian,
        'series':series,
        'categories':categories,
    }
    return render(request,'app/index.html' , context)

def category(request, slug_category):
    category = Category.objects.get(slug = slug_category)
    movies = Movie.objects.filter(category = category)
    series = Serie.objects.filter(category = category)
    videos = list(chain(movies, series))
    return render(request,'app/category.html' , {'videos':videos, 'category':category})

def search(request):
    if request.method == "GET":
        if request.GET.get('query') is not None:
            query = request.GET.get('query')
            resultMovies = Movie.objects.filter(title__icontains=query)
            resultSeries = Serie.objects.filter(title__icontains=query)
            resultMoviesAr = Movie.objects.filter(title_ar__icontains=query)
            results = chain( resultMovies,resultSeries,resultMoviesAr)
    return render(request,'app/results.html' , {'results':results})

def movies(request):
    categories = Category.objects.filter(slug__icontains='movies').order_by('name')
    movies = Movie.objects.all()
    return render(request,'app/movies.html' , {'movies':movies, 'categories':categories})

def series(request):
    categories = Category.objects.filter(slug__icontains='series').order_by('name')
    series = Serie.objects.filter(is_tvshow=False)
    return render(request,'app/series.html' , {'series':series, 'categories':categories})

def tvshows(request):
    categories = Category.objects.filter(slug__icontains='tvshows').order_by('name')
    tvshows = Serie.objects.filter(is_tvshow=True)
    return render(request,'app/tvshows.html' , {'tvshows':tvshows, 'categories':categories})

def movie(request, pk):
    try :
        movie  = get_object_or_404(Movie, id=pk )
    except Http404:
        raise Http404("Page Not Found")
    return render(request, 'app/movie.html', {'movie':movie})

def serie(request, pk):
    try :
        serie  = get_object_or_404(Serie, id=pk )
        episodes = Episode.objects.filter(serie=serie)
    except Http404:
        raise Http404("Page Not Found")
    return render(request, 'app/serie.html', {'serie':serie, 'episodes':episodes})

def watch(request, pk):
    try :
        movie  = get_object_or_404(Movie, id=pk )
    except Http404:
        raise Http404("Page Not Found")
    videolinks = {1:movie.link1, 2:movie.link2, 3:movie.link3}
    videolink = movie.link1
    return render(request, 'app/watch.html', {'movie':movie, 'videolinks':videolinks, 'videolink':videolink})

def watchepisode(request, pk):
    try :
        episode = get_object_or_404(Episode, id=pk)
        serie = Serie.objects.get(id = episode.serie.id)
    except Http404:
        raise Http404("Page Not Found")
    videolinks = {1:episode.link1, 2:episode.link2, 3:episode.link3}
    videolink = episode.link1
    return render(request, 'app/watchepisode.html', {'episode':episode, 'serie':serie, 'videolinks':videolinks, 'videolink':videolink})

def playvideo(request):
    videolink = "https://www.youtube.com/embed/5bY5IarNPuk"
    if request.method == "POST":
        videolink = request.POST.get('videolink')
    print(videolink)
    return render(request, 'app/playvideo.html', {'videolink':videolink})

def latestmovies(request):
    movies = Movie.objects.all()[:24][::-1]
    return render(request, 'app/latestmovies.html', {'movies':movies})

def latestepisodes(request):
    episodes = Episode.objects.all()[:24][::-1]
    return render(request, 'app/latestepisodes.html', {'episodes':episodes})
