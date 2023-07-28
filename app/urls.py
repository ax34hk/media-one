from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('MovieVSet', MovieViewset)

app_name = 'app'

urlpatterns = [
    path('api/', include(router.urls)),
    path('test/', test, name='test'),
    path('testcat/<slug:slug_category>/', testcat, name='testcat'),
    path('search/', search, name='search'),
    path('movies/', movies, name='movies'),
    path('series/', series, name='series'),
    path('tvshows/', tvshows, name='tvshows'),
    path('movie/<int:pk>/', movie, name='movie'),
    path('testmovie/<int:pk>/', testmovie, name='movie'),
    path('watch/<int:pk>/', watch, name='watch'),

]