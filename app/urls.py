from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('MovieVSet', MovieViewset)

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('test/', test, name='test'),
    path('movie/<int:pk>/', movie, name='movie'),
    path('submovies/<slug:slug_category>/', submovies, name='submovies'),
    path('api/', include(router.urls)),
]