from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from movie.models import Movie
# from movie.views import home, category, search, MovieDetail


class MovieViewsTest(TestCase):
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
                                         image="movie/static/img/bg/bg.jpg",
                                         movie_story="sdhsgihhsigh iishgiiusn",
                                         download_link="lghhg jsdghsgopiohfs")

    def tearDown(self):
        self.movie = None

    def test_home_view(self):
        # One method of using client without import
        url = reverse("home")
        view = self.client.get(url)
        self.assertEqual(view.status_code, 200)
        self.assertTemplateUsed(view, "movie_home.html")

    def test_search_view(self):
        # Another method of using client
        self.client = Client()
        view = self.client.get(reverse("search"))
        self.assertEqual(view.status_code, 200)
        self.assertTemplateUsed(view, "search.html")

    def test_category_view(self):
        url = reverse("category", args=["telugu"])
        view = self.client.get(url)
        self.assertEqual(view.status_code, 200)
        self.assertTemplateUsed(view, "movie_category.html")

    # def test_detail_view(self):
    #     url = reverse(MovieDetail, args=['don-telugu-hdrip'])
    #     view = self.client.get(url)
    #     self.assertEqual(view.status_code, 200)
    #     self.assertTemplateUsed(view, "movie_category.html")
