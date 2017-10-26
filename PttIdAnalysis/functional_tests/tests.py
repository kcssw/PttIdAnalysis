# -*- coding: utf-8 -*-
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

from datetime import datetime
import time
import uuid

from historical_records.models import Article

MAX_WAIT = 10

class HistoricalRecordsTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver.exe')

    def tearDown(self):
        # Satisfied, she goes back to sleep
        self.browser.quit()

    def save__all_articles(self):
        for article in self.postedArticles:
            article.save()

        for article in self.commentedArticles:
            article.save()

    def test_can_display_all_posted_articles(self):
        # Arvin has heard about a cool new online app.
        # He goes to check out this homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title, 'PTTUserAnalysis' and header mention 'Retrieve User Historical Articles'
        self.assertIn('PTTUserAnalysis', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Retrieve User Historical Articles', header_text)

        # He is invited to enter a PTT ID and also the query article type
        inputbox = self.browser.find_element_by_id('id_query_user')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a user ID'
        )
        selectBox = self.browser.find_element_by_id('id_query_article_type')
        optionTexts = []
        options = selectBox.find_elements_by_tag_name('option')
        for option in options:
            if option.text == 'Posted Articles':
                self.assertTrue(option.get_attribute('selected'))
            else:
                self.assertFalse(option.get_attribute('selected'))
            optionTexts.append(option.text)
        self.assertEqual(3, len(optionTexts))
        self.assertIn('Posted Articles', optionTexts)
        self.assertIn('Commented Articles', optionTexts)
        self.assertIn('Posted Articles And Commented Articles', optionTexts)

        #  He types "obov" into a text box and select 'Posted Articles' in the drop box
        inputbox.send_keys('obov')
        for option in options:
            if option.text == 'Posted Articles':
                option.click()

        #  When he hits enter, the page updates, and now the page lists titles of 50 articles posted by obov
        #  He notices that page title is updated to obov's page
        #  He clicks one interesting article and the page displays the article.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.assertIn('obov', self.browser.title)
        table = self.browser.find_element_by_id('id_article_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertGreater(len(rows), 1)
        self.assertLessEqual(len(rows), 50)
        self.assertTrue(any(row.text == u'1: Re: [問卦] 有沒有醫學系要兼修心理學的八卦' for row in rows))

        #  He returns the page displays all posted articles again.
        #  He click 'Next' button and the page displays the next 50 articles.

        #  Then, Arvin wants to check all articles commented by obov.
        #  He selects another item, 'Commented Articles' in the drop box.
        self.fail('Finish the test!')

        # When he hits enter, the page updates, and now the page lists titles of 50 articles commented by obov
        #  Besides, the page shows obov's comments of each displayed article.
        #  He also click the article and return to the app again.
        #  Thne, click 'Next' button to check the next 50 articles and comments and click 'back' to check the original 50 articles.

        # Arvin wants to check posted and commented articles and select 'Posted and Commented Articles.'

        #  When he hits enter, the page updates, and now the page lists titles of 50 articles posted or commented by obov.
        #  Besides, the page shows obov's comments of each displayed article.
        #  He also click the article and return to the app again.
        #  Thne, click 'Next' button to check the next 50 articles and comments and click 'back' to check the original 50 articles.

class Comment:
    article = None
    content = None
    timestamp = None
    author = None