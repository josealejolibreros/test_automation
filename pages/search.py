from selenium.webdriver.common.by import By

class GoogleSearchPage:

    URL = "https://google.com"
    SEARCH_INPUT = (By.NAME, 'q')

    def __init__(self, browser):
        self.browser = browser
    def load(self):
        self.browser.get(self.URL)
    def search(self, phrase):

        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
        script_text = "var searchButton = document.getElementsByName(\"btnK\")[1]; searchButton.click();"
        try:
            self.browser.execute_script(script_text)
        except:
            pass
