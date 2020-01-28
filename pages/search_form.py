from selenium.webdriver import Firefox

from locators.search_form import SearchFormLocators
from pages.result_page import ResultPage


class SearchForm(SearchFormLocators):

    def __init__(self, browser = None):
        self.browser = browser or Firefox()
    
    def __enter__(self):
        return self
    
    def __exit__(self, *exc):
        return False
    
    def do_feeling_lucky_search(self, query) -> ResultPage:
        self.type_query(query)
        self.submit_feeling_lucky_search()
        return ResultPage(self.browser)
    
    def do_normal_search(self, query) -> ResultPage:
        self.type_query(query)
        self.submit_normal_search()
        return ResultPage(self.browser)
    
    def submit_feeling_lucky_search(self):
        return self._click_submit(self.LUCKY_SEARCH_BTN)
    
    def submit_normal_search(self):
        return self._click_submit(self.NORMAL_SEARCH_BTN)
    
    def type_query(self, query):
        return self._set_query_text(query)
        
    def _click_submit(self, btn_locator):
        self.browser.click(btn_locator)
        return self
    
    def _set_query_text(self, query):
        self.browser.input_field(self.SEARCH_BOX, query)
        return self