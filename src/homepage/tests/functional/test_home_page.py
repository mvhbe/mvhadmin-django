import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        """home page werkt zoals verwacht"""
        # administrator opent de site
        self.browser.get("http://localhost:8000/mvhadmin/")
        # administrator ziet "MvhAdmin" als titel in de browser
        self.assertIn('MvhAdmin', self.browser.title)
        # administrator ziet een menu (paneel) voor ingave
        ingave_menu = self.browser.find_element_by_id("ingave-menu")
        self.assertIsNotNone(ingave_menu)
        # administrator ziet een paneel voor beheer
        beheer_menu = self.browser.find_element_by_id("beheer-menu")
        self.assertIsNotNone(beheer_menu)

if __name__ == "__main__":
    unittest.main()
