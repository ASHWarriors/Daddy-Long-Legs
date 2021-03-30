# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 20:44:53 2021

@author: Sristi
"""


from django.http import HttpResponse
from django.template import loader
from django.template.loader import render_to_string
from django.template import engines
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from DaddyLongLegs import upgcinfo
from DaddyLongLegs import Money
from DaddyLongLegs import webparsing
#from gcinfo import *
#from webparsing import *
# from suject_match import *
#from upgcinfo import *
from DaddyLongLegs import surplus_funds
#from DaddyLongLegs import collect





@csrf_exempt

def totf(request):
    f=open('buffer.txt','r')
    name,budget,preference=f.readlines()
    f.close()
    mypart,yourpart=surplus_funds.BankKnows(float(budget),preference)
    cont=(yourpart/mypart)*100    
       
    




    about='''
    <html>
    {% load static %}
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    body {
      font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
      background-image: url("{% static 'Images/child.jpg'%}");
      background-size: cover;
    }
    
    * {
      box-sizing: border-box;
    }
    .container {
      padding: 16px;
      background-color: rgb(19, 162, 228);
      background-image: url("{% static 'Images/pink.jpg'%}");
      height: 600px; 
      background-position: center;
      background-repeat: no-repeat; 
      background-size: cover;
      text-align: center;
      align-items: center;
    }
    
    .center {
      margin: 0;
      position: absolute;
      top: 40%;
      left: 50%;
      -ms-transform: translate(-50%, -50%);
      transform: translate(-50%, -50%);
    }
    
    </style>
    </head>
    <body>
    
    <div class="container">
       
       
        <div class ="center">
            <h1><b>THANKS TO YOU '''+name+''' , OUR TOTAL FUNDS ARE:'''+str(mypart)+''' 
            Congratulations! You contributed '''+str(cont)+''' %</b></h1>
        </div>
    </div>
    <br><br>
    
    
    </body>
    </html>'''
    django_engine=engines['django']
    template=django_engine.from_string(about)
    html=template.render()
    return HttpResponse(html) 
        
    
    
