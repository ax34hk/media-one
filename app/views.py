from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from .models import Movie, Category, Serie
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieSerializer
from django.contrib import messages


# def index(request):
#     movies = Movie.objects.all()
#     return render(request,'app/index.html' , {'movies':movies})

# def movie(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     return render(request,'app/movie.html' , {'movie':movie})

# def submovies(request, slug_category):
#     category = Category.objects.get(slug = slug_category)
#     movies = Movie.objects.filter(category = category)
#     return render(request,'app/submovies.html' , {'movies':movies, 'category':category})

class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

def test(request):
    categories = Category.objects.order_by('name')
    movies = Movie.objects.all()
    return render(request,'app/test.html' , {'movies':movies, 'categories':categories})

def testcat(request, slug_category):
    category = Category.objects.get(slug = slug_category)
    movies = Movie.objects.filter(category = category)
    return render(request,'app/test-cat.html' , {'movies':movies, 'category':category})

def search(request):
    if request.method == "GET":
        if request.GET.get('query') is not None:
            query = request.GET.get('query')
            resultMovies = Movie.objects.filter(title__icontains=query)
    return render(request,'app/results.html' , {'resultMovies':resultMovies})

def movies(request):
    categories = Category.objects.filter(slug__icontains='movies').order_by('name')
    movies = Movie.objects.all()
    return render(request,'app/testmovies.html' , {'movies':movies, 'categories':categories})

def series(request):
    categories = Category.objects.filter(slug__icontains='series').order_by('name')
    series = Serie.objects.filter(is_tvshow=False)
    return render(request,'app/testseries.html' , {'series':series, 'categories':categories})

def tvshows(request):
    categories = Category.objects.filter(slug__icontains='tvshows').order_by('name')
    tvshows = Serie.objects.filter(is_tvshow=True)
    return render(request,'app/testtvshows.html' , {'tvshows':tvshows, 'categories':categories})

def movie(request, pk):
    try :
        movie  = get_object_or_404(Movie, id=pk )
    except Http404:
        raise Http404("Page Not Found")
    return render(request, 'app/movie.html', {'movie':movie})

def testmovie(request, pk):
    try :
        movie  = get_object_or_404(Movie, id=pk )
    except Http404:
        raise Http404("Page Not Found")
    return render(request, 'app/testmovie.html', {'movie':movie})

def watch(request, pk):
    try :
        movie  = get_object_or_404(Movie, id=pk )
    except Http404:
        raise Http404("Page Not Found")
    return render(request, 'app/watch.html', {'movie':movie})
