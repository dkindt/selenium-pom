from abc import (ABCMeta, abstractmethod, )
from locators.base import PageLocators


class PageObject(metaclass=ABCMeta):

    @property
    @abstractmethod
    def urls(self):
        return None
    
    @abstractmethod
    def is_loaded(self):
        return False
    
    @abstractmethod
    def load(self):
        pass


class BasePage(PageObject, PageLocators):

    def __init__(self, browser, urls):
        self.browser = browser
        self.urls = urls
        self.load()
        self.is_loaded()
    
    def is_loaded(self):
        return False
    
    def load(self):
        pass