# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 01:33:13 2021

@author: Sristi
"""
##################################################################################
#This part is only dedicated to Django, when we get info from user we'll manage that here
from django.http import HttpResponse
from django.template import loader
def Gc(request):
    template=loader.get_template('child.html')
    return HttpResponse(template.render())

###################################################################################
