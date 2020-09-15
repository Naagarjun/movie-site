from django.test import TestCase
from django.urls import reverse, resolve


class TestMovieUrls(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_home_url(self):
        self.url = reverse('home')
        self.assertTrue(resolve(self.url).func, "home")

    def test_search_url(self):
        self.url = reverse('search')
        self.assertTrue(resolve(self.url).func, "search")

    def test_category_url(self):
        self.url = reverse('category', args=["telugu"])
        self.assertTrue(resolve(self.url).func, "category")
