from django.shortcuts import render
from django.db.models import Q
from django.views.generic import DetailView

from movie.models import Movie

# Create your views here.


def home(request):
    context = {
        'movies': Movie.movies.all()
    }
    return render(request, 'movie_home.html', context)


def category(request, category):
    context = {
        "movies": Movie.movies.filter(category=category)
    }
    return render(request, "movie_category.html", context)


def search(request):
    if request.method == "GET":
        query = request.GET.get("q")
        if query is not None:
            results = Movie.movies.filter(Q(name__icontains=query)).distinct()
            context = {
                'results': results
            }
            return render(request, "search.html", context)
        else:
            return render(request, "search.html")

    else:
        return render(request, "search.html")


class MovieDetail(DetailView):
    model = Movie
    template_name = "movie_detail.html"
    lookup_field = "slug"
    context_object_name = "movie"


def index(request):
    context = {
        'movies': Movie.movies.all()
    }
    return render(request, "index.html", context)
