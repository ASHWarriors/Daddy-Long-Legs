# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 00:45:45 2021

@author: Sristi
"""

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from DaddyLongLegs import MASTER
from DaddyLongLegs import dbchild

@csrf_exempt

def Rgs(request):
    
    if request.method=='POST':
        
        name=request.POST.get('name')
        age=request.POST.get('age')
        subj=request.POST.get('sub')
        grade=request.POST.get('grade')
        email=request.POST.get('email')
        child=","
        child=child.join(MASTER.entry([name,age,email,"NULL"]))
        print(child)
        
        child2=[name,grade,subj,email]
        print(child2)
        MASTER.IamChild(child,child2)
        
        template=loader.get_template('Reg.html')
        return HttpResponse(template.render())