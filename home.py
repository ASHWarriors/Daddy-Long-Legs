# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 15:29:46 2021

@author: Sristi
"""
from .static.Images import *
from django.http import HttpResponse
from django.template import loader
from django.template import engines
from django.template.loader import render_to_string

def home(request):
    template=loader.get_template('soon.html')
    return HttpResponse(template.render())
