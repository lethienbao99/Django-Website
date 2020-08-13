from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse


class Actor(models.Model):
    name = models.CharField(max_length=30)
    photo = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(default="", unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=150)
    photo = models.URLField(default="", blank=True)
    minute = models.CharField(max_length=50)
    video = models.URLField(default="", blank=True)
    description = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    actors = models.ManyToManyField(Actor)
    slug = models.SlugField(default="", unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("movie-detail", kwargs={"slug": self.slug})
