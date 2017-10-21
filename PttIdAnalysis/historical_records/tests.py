# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')