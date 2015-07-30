import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        """home page bereikbaar ?"""
        self.browser.get("http://localhost:8000")
        self.assertIn('MvhAdmin', self.browser.title)
        
if __name__ == "__main__":
    unittest.main()