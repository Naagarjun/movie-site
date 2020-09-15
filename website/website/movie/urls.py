from django.urls import path
from movie.views import (home, category, MovieDetail, search, index)

urlpatterns = [
    path('', home, name='home'),
    path("movie-category/<str:category>/", category, name="category"),
    path("movie/<str:slug>/", MovieDetail.as_view(), name="movie-detail"),
    path('search/', search, name="search"),
    path('index/', index),
]
