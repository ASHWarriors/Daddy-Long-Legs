# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 16:20:54 2021

@author: Sristi
"""

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def lg(request):
    template=loader.get_template('logpg.html')
    return HttpResponse(template.render())
