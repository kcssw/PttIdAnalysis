# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from datetime import datetime
import time
import uuid

from historical_records.models import Article

class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class UserArticlesTest(TestCase):

    def setUp(self):
        for article in Article.objects.all():
            article.delete()

    def test_user_id_resolve_to_user_articles_page_view(self):
        response = self.client.get('/PostedArticles/obov')
        self.assertTemplateUsed(response, 'user_articles.html')

    def test_saving_and_retrieving_posted_articles(self):
        first_article = Article()
        first_article.id = uuid.uuid4()
        first_article.title = 'The first (ever) article'
        first_article.posted_time = datetime(2017, 1, 10, 13, 43, 18, 0)
        first_article.author = 'obov'
        first_article.url = 'localhost:8000'
        first_article.save()

        second_article = Article()
        second_article.id = uuid.uuid4()
        second_article.title = 'Article the second'
        second_article.posted_time = datetime(2016, 12, 26, 16, 59, 10, 0)
        second_article.author = 'obov'
        second_article.url = 'localhost:8000'
        second_article.save()

        saved_articles = Article.objects.all()
        self.assertEqual(saved_articles.count(), 2)

        first_saved_article = saved_articles[0]
        second_saved_article = saved_articles[1]
        titles = [first_saved_article.title, second_saved_article.title]
        self.assertIn('The first (ever) article', titles)
        self.assertIn('Article the second', titles)
        self.assertEqual(first_saved_article.author, 'obov')
        self.assertEqual(second_saved_article.author, 'obov')
        self.assertEqual(first_article.posted_time, datetime(2017, 1, 10, 13, 43, 18, 0))
        self.assertEqual(second_article.posted_time, datetime(2016, 12, 26, 16, 59, 10, 0))
        self.assertEqual(first_article.url, 'localhost:8000')
        self.assertEqual(second_article.url, 'localhost:8000')

    def test_saving_and_retrieving_commented_articles(self):
        first_article = Article()
        first_article.id = uuid.uuid4()
        first_article.title = 'The first (ever) article'
        first_article.posted_time = datetime(2017, 1, 10, 13, 43, 18, 0)
        first_article.author = 'arvin'
        first_article.url = 'localhost:8000'
        first_article.commenter = 'obov'
        first_article.comments = 'say something'
        first_article.save()

        second_article = Article()
        second_article.id = uuid.uuid4()
        second_article.title = 'Article the second'
        second_article.posted_time = datetime(2016, 12, 26, 16, 59, 10, 0)
        second_article.author = 'obov'
        second_article.url = 'localhost:8000'
        second_article.commenter = 'arvin'
        second_article.comments = 'say something again'
        second_article.save()

        saved_articles = Article.objects.all()
        self.assertEqual(saved_articles.count(), 2)

        ids = [saved_articles[0].id, saved_articles[1].id]
        self.assertIn(first_article.id, ids)
        self.assertIn(second_article.id, ids)

        first_saved_article = saved_articles[0] if saved_articles[0].id == first_article.id else saved_articles[1]
        second_saved_article = saved_articles[1] if saved_articles[1].id == second_article.id else saved_articles[0]

        self.assertEqual(first_saved_article.title, 'The first (ever) article')
        self.assertEqual(second_saved_article.title, 'Article the second')
        self.assertEqual(first_saved_article.author, 'arvin')
        self.assertEqual(second_saved_article.author, 'obov')
        self.assertEqual(first_article.posted_time, datetime(2017, 1, 10, 13, 43, 18, 0))
        self.assertEqual(second_article.posted_time, datetime(2016, 12, 26, 16, 59, 10, 0))
        self.assertEqual(first_article.url, 'localhost:8000')
        self.assertEqual(second_article.url, 'localhost:8000')
        self.assertEqual(first_article.commenter, 'obov')
        self.assertEqual(second_article.commenter, 'arvin')
        self.assertEqual(first_article.comments, 'say something')
        self.assertEqual(second_article.comments, 'say something again')