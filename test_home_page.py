import unittest

from selenium.webdriver import Firefox

from pages.search_form import SearchForm


class TestGoogleHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = Firefox()

    def test_normal_search_success(self):
        with SearchForm(self.browser) as form:
            result_page = form.do_normal_search("Galileo Financial Technologies")
