from locators.result_page import ResultPageLocators


class ResultPage(ResultPageLocators):

    def __init__(self, browser, original_query: str = None):
        self.browser = browser
        self.query = original_query
