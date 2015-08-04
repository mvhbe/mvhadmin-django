from django.http import HttpRequest
from django.test import TestCase
from homepage.views import home_page


class HomePageViewTest(TestCase):

    def test_home_page_heeft_titel(self):
        """Titel home page is 'MvhAdmin'"""
        request = HttpRequest()
        response = home_page(request)
        self.assertIn('MvhAdmin', response.content.decode("utf8"))

    def test_home_page_heeft_menu_voor_ingeven_data(self):
        """Titel home page heeft menu voor ingeven data"""
        request = HttpRequest()
        response = home_page(request)
        content = response.content.decode('utf8')
        self.assertIn('id="ingave-menu" class="panel', content)

    def test_home_page_heeft_menu_voor_beheren_data(self):
        """Titel home page heeft menu voor beheren data"""
        request = HttpRequest()
        response = home_page(request)
        content = response.content.decode('utf8')
        self.assertIn('id="beheer-menu" class="panel', content)
