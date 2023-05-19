from django.shortcuts import render
from .models import Movie, Category
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieSerializer


def index(request):
    movies = Movie.objects.all()
    return render(request,'app/index.html' , {'movies':movies})

def movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request,'app/movie.html' , {'movie':movie})

def submovies(request, slug_category):
    category = Category.objects.get(slug = slug_category)
    movies = Movie.objects.filter(category = category)
    return render(request,'app/submovies.html' , {'movies':movies, 'category':category})

class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)



def test(request):
    return render(request,'app/test.html')