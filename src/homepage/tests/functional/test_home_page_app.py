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
        # administrator ziet "Mvh Administratie" als titel in de browser
        self.assertIn('Mvh Administratie', self.browser.title)
        
if __name__ == "__main__":
    unittest.main()
