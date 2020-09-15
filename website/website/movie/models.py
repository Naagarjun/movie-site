from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


category_choices = [('Telugu', 'Telugu'), ('Tamil', 'Tamil'),
                    ('Kannada', 'Kannada'), ('Bollywood', 'Bollywood'),
                    ('Hollywood', 'Hollywood')]


class Movie(models.Model):
    movies = models.Manager()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=15, choices=category_choices)
    name = models.CharField(max_length=256)
    image = models.ImageField()
    size = models.CharField(max_length=15)
    resolution = models.CharField(max_length=15)
    director = models.CharField(max_length=50)
    cast = models.CharField(max_length=100)
    genres = models.CharField(max_length=15)
    movie_story = models.TextField()
    download_link = models.CharField(max_length=256)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
