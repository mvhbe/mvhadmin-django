from django.http import HttpRequest
from django.test import TestCase
from homepage.views import home_page


class HomePageViewTest(TestCase):

    def test_home_page_heeft_titel(self):
        """Titel home page is 'Mvh Administration'"""
        request = HttpRequest()
        response = home_page(request)
        self.assertIn('Mvh Administratie', response.content.decode("utf8"))
