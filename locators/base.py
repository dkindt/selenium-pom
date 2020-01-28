import threading
from typing import Optional
import unittest

from selenium.webdriver.common.by import By


ALLOWED_STRATEGIES = (
    By.CLASS_NAME,
    By.CSS_SELECTOR,
    By.ID,
    By.LINK_TEXT,
    By.NAME,
    By.PARTIAL_LINK_TEXT,
    By.TAG_NAME,
    By.XPATH,
)


class SingletonMeta(type):

    _instance: Optional[type] = None
    _lock: threading.Lock = threading.Lock()

    def __call__(mcs, *args, **kwargs):
        with mcs._lock:
            if mcs._instance is None:
                mcs._instance = super().__call__(mcs, *args, **kwargs)
        return mcs._instance


class Singleton(metaclass=SingletonMeta):
    pass


class PageLocators(Singleton):
    pass


class InvalidStrategyError(ValueError):

    def __init__(self, strategy, *args, **kwargs):
        super().__init__(*args)
        self.msg = f"Strategy value must be: {'|'.join(ALLOWED_STRATEGIES)}"
        self.strategy = strategy


def validate_strategy(strategy):
    if isinstance(strategy, str):
        by = strategy.lower()
        if by in ALLOWED_STRATEGIES:
            return by
    raise InvalidStrategyError(strategy)


class Strategy(type):

    def __new__(mcs, name, bases, namespace):
        if bases:
            try:
                validate_strategy(namespace["by"])
            except KeyError as e:
                raise NotImplementedError(
                    "Class variable 'by' is required") from e
        namespace["__slots__"] = ("by", "locator", )
        return super().__new__(mcs, name, bases, namespace)


class Locator(metaclass=Strategy):

    def __init__(self, locator):
        self.locator = locator


class FindBy(Locator):

    def __get__(self, instance, owner):
        return (self.by, self.locator)

    def __set__(self, instance, value):
        instance.__dict__[self.key] = value
    
    def __set_name__(self, owner, name):
        # Name of the attribute being stored.
        # This is the key in the instance dict.
        self.key = name
    
    def __delete__(self, instance):
        # TODO: might be overkill, because of how `__get__`
        #       was implemented (returns a tuple)
        raise AttributeError("Cannot delete the attribute")


class XPath(FindBy):
    by = By.XPATH


class CSS(FindBy):
    by = By.CSS_SELECTOR


class Name(FindBy):
    by = By.NAME


