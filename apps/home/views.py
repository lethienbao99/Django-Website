from django.http import HttpResponse
from django.shortcuts import render
from apps.movies.models import Movie
from django.views.generic import ListView


class HomeListView(ListView):
    model = Movie
    queryset = Movie.objects.order_by("date")
    context_object_name = "movie_list"
    template_name = "home/index.html"
    paginate_by = 8
