# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.shortcuts import render

from historical_records.models import Article

def home_page(request):
    return render(request, 'home.html')

def user_articles(request, author_id):
    articles = Article.objects.filter(author=author_id)
    for article in articles:
        print 'test', article.title
    return render(request, 'user_articles.html', {'author' : author_id, 'articles': articles})

def query_articles(request):
    author = request.POST.get('author_id', '')
    return redirect('/post_articles/' + str(author))
