class SearchFormLocators:
    # Google search form locators
    SEARCH_BOX = Name("q")
    NORMAL_SEARCH_BTN = CSS("#tsf .FPdoLc [value='Google Search']")
    LUCKY_SEARCH_BTN = XPath('(//input[@value="I\'m Feeling Lucky"])[2]')