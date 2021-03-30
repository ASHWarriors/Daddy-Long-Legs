# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 01:34:35 2021

@author: Sristi
"""
from django.views.decorators.csrf import csrf_exempt
#from django.views.decorators.csrf import csrf_protect

from django.http import HttpResponse
from django.template import loader
from django.template import engines

@csrf_exempt

def form(request):
    #if request.method=='POST':
    if 'financial' in request.POST:
        template=loader.get_template('fin.html')
    elif 'voluntary' in request.POST:
        template=loader.get_template('band1.html')
    django_engine=engines['django']   
    return HttpResponse(template.render())    
     