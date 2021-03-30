# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 13:12:23 2021

@author: Sristi
"""


from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from DaddyLongLegs import MASTER
from DaddyLongLegs import dbchild

@csrf_exempt

def Nonvolun(request):
    template=loader.get_template('band1.html')
    return HttpResponse(template.render())
    