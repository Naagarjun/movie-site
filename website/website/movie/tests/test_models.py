from django.test import TestCase
from movie.models import Movie
from django.contrib.auth.models import User


class MovieModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="admin", password="Nag_arjun@33", email="admin@test.com")
        self.movie = Movie.movies.create(author=self.user,
                                         category="telugu",
                                         name="Don telugu hdrip",
                                         size="1.2GB",
                                         resolution="360P", director="gowtham",
                                         cast="nani, shraddha",
                                         genres='sports,drama',
                                         movie_story="sdhsgihhsigh iishgiiusn",
                                         download_link="lghhg jsdghsgopiohfs")

    def test_movie_name_matching(self):
        self.assertTrue(isinstance(self.movie, Movie))
        self.assertEqual(self.movie.name, 'Don telugu hdrip')

    def tearDown(self):
        self.movie = None
