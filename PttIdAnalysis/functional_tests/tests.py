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

        postedArticle1 = Article()
        postedArticle1.id = uuid.uuid4()
        postedArticle1.title = 'Re: [問卦] 有沒有醫學系要兼修心理學的八卦'
        postedArticle1.timestamp = datetime(2017, 1, 10, 13, 43, 18, 0)
        postedArticle1.author = 'obov'
        postedArticle1.save()
        postedArticle2 = Article()
        postedArticle2.id = uuid.uuid4()
        postedArticle2.title = 'Re: [問卦] obov隱退了嗎'
        postedArticle2.timestamp = datetime(2016, 12, 26, 16, 59, 10, 0)
        postedArticle2.author = 'obov'
        postedArticle2.save()
        postedArticle3 = Article()
        postedArticle3.id = uuid.uuid4()
        postedArticle3.title = '[測試] 你還在寫計網作業嗎？'
        postedArticle3.timestamp = datetime(2016, 12, 03, 23, 35, 51, 0)
        postedArticle3.author = 'obov'
        postedArticle3.save()
        self.postedArticles = [postedArticle1, postedArticle2, postedArticle3]

        saved_articles = Article.objects.all()
        for article in saved_articles:
            print article.title

        commentedArticle1 = Article()
        commentedArticle1.title = 'Re: [閒聊] 神劍把雪代緣的部份砍掉會更接近神作嗎?'
        commentedArticle1.timestamp = datetime(2016, 12, 1, 15, 16, 22, 0)
        commentedArticle1.author = 'abc'
        commentedArticle2 = Article()
        commentedArticle2.title = '[閒聊] 女孩兒喜歡刪推文刪全部嗎'
        commentedArticle2.timestamp = datetime(2016, 11, 25, 1, 45, 13, 0)
        commentedArticle2.author = 'def'
        commentedArticle3 = Article()
        commentedArticle3.title = 'Re: [心情]我覺得男版待不下去了'
        commentedArticle3.timestamp = datetime(2016, 11, 22, 11, 13, 46, 0)
        commentedArticle3.author = 'ghi'
        self.commentedArticles = [commentedArticle1, commentedArticle2, commentedArticle3]

        comment1 = Comment()
        comment1.author = 'obov'
        comment1.content = '123456'
        comment2 = Comment()
        comment2.author = 'obov'
        comment2.content = '7891011'
        comment3 = Comment()
        comment3.author = 'abc'
        comment3.content = '12131415'
        comment4 = Comment()
        comment4.author = 'obov'
        comment4.content = '16171819'
        comment5 = Comment()
        comment5.author = 'def'
        comment5.content = '20212223'
        comment6 = Comment()
        comment6.author = 'ghi'
        comment6.content = '242526'

        postedArticle1.comments = []
        postedArticle2.comments = []
        postedArticle3.comments = []

        commentedArticle1.comments = [comment1]
        commentedArticle2.comments = [comment2, comment3]
        commentedArticle3.comments = [comment4, comment5, comment6]

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
        for article in self.postedArticles:
            self.assertTrue(any(row.text == article.title for row in rows))

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