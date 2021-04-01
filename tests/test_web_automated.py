from pages.result import GoogleResultPage
from pages.search import GoogleSearchPage
from selenium.webdriver import Chrome
import time
import unittest

class TestCar(unittest.TestCase):
    def setUp(self):

        driver = Chrome()

        driver.implicitly_wait(10)

        # Return the driver object at the end of setup
        self.browser = driver

        # For cleanup, quit the driver
        #driver.quit()


    def test_google_search(self):
        PHRASE = 'test automation'
        CONDITION = 'automation'

        search_page = GoogleSearchPage(self.browser)
        time.sleep(5)
        search_page.load()

        search_page.search(PHRASE)

        time.sleep(2)

        result_page = GoogleResultPage(self.browser)
        results = result_page.link_phrases()
        len_results = len(results)

        text_link = ''
        condition_in_text = False
        for result in results:
            text_link = result.find_element_by_tag_name('h3').text.lower()

            if CONDITION in text_link:
                condition_in_text = True
                link = result.find_element_by_tag_name('a')
                link.click()
                time.sleep(2)
                break

        self.assertEqual(result_page.get_title() , text_link)
        self.assertTrue(condition_in_text)
        self.assertGreater(len_results, 0)