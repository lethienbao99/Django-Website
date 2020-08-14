from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Movie


def index(request):
    return render(request, 'movies/movie-list.html')


class MovieDetailView(DetailView):
    model = Movie
    slug_url_kwarg = "the_slug"
    context_object_name = "movie"
    slug_field = "slug"
    template_name = "movies/movie-detail.html"


class MovieListView(ListView):
    model = Movie
    queryset = Movie.objects.order_by("date")
    context_object_name = "movie-list"
    template_name = "movies/movie-list.html"
    paginate_by = 10
