# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 01:28:06 2021

@author: Sristi
"""

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Gp(request):
    
    template=loader.get_template('wp2.html')
    
    return HttpResponse(template.render())