# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')
