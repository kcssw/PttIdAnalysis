from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

import time

MAX_WAIT = 10

class HistoricalRecordsTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver.exe')

    def tearDown(self):
        # Satisfied, she goes back to sleep
        self.browser.quit()

    def test_can_display_all_posted_articles(self):
        # Arvin has heard about a cool new online app.
        # He goes to check out this homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title, 'PTTUserAnalysis' and header mention 'Retrieve User Historical Articles'
        self.assertIn('PTTUserAnalysis', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Retrieve User Historical Articles', header_text)

        # He is invited to enter a PTT ID

        #  He types "Obov" into a text box and select 'Posted Articles' in the drop box

        #  When he hits enter, the page updates, and now the page lists titles of 50 articles posted by obov
        #  He clicks one interesting article and the page displays the article.
        #  He returns the page displays all posted articles again.
        #  He click 'Next' button and the page displays the next 50 articles.

        #  Then, Arvin wants to check all articles commented by obov.
        #  He selects another item, 'Commented Articles' in the drop box.

        # When he hits enter, the page updates, and now the page lists titles of 50 articles commented by obov
        #  Besides, the page shows obov's comments of each displayed article.
        #  He also click the article and return to the app again.
        #  Thne, click 'Next' button to check the next 50 articles and comments and click 'back' to check the original 50 articles.

        # Arvin wants to check posted and commented articles and select 'Posted and Commented Articles.'

        #  When he hits enter, the page updates, and now the page lists titles of 50 articles posted or commented by obov.
        #  Besides, the page shows obov's comments of each displayed article.
        #  He also click the article and return to the app again.
        #  Thne, click 'Next' button to check the next 50 articles and comments and click 'back' to check the original 50 articles.