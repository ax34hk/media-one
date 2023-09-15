from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('MovieVSet', MovieViewset)

app_name = 'app'

urlpatterns = [
    path('api/', include(router.urls)),
    path('', index, name='index'),
    path('category/<slug:slug_category>/', category, name='category'),
    path('search/', search, name='search'),
    path('movies/', movies, name='movies'),
    path('series/', series, name='series'),
    path('tvshows/', tvshows, name='tvshows'),
    path('latestmovies/', latestmovies, name='latestmovies'),
    path('latestepisodes/', latestepisodes, name='latestepisodes'),
    path('movie/<uuid:pk>/', movie, name='movie'),
    path('serie/<uuid:pk>/', serie, name='serie'),
    path('watch/<uuid:pk>/', watch, name='watch'),
    path('watchepisode/<uuid:pk>/', watchepisode, name='watchepisode'),
    path('playvideo/', playvideo, name='playvideo'),


]