from selenium.webdriver.common.by import By



class GoogleResultPage:
    LINK_DIVS = 'rso'
    LINK_PHRASES = 'g'
    SEARCH_INPUT = (By.ID, 'search_form_input')

    def __init__(self, browser):
        self.browser = browser

    def link_phrases(self):
        link_divs = self.browser.find_element_by_id(self.LINK_DIVS)
        results = link_divs.find_elements_by_class_name(self.LINK_PHRASES)
        return results

    def get_title(self):
        title = self.browser.title.lower()
        return title
