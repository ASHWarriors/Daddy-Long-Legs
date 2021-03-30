# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 13:22:34 2021

@author: Sristi
"""





from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from DaddyLongLegs import MASTER
from DaddyLongLegs import dbchild
from DaddyLongLegs import submatch
from django.template.loader import render_to_string
from django.template import engines
from django.template import RequestContext
from DaddyLongLegs import update
from DaddyLongLegs import waitlist
@csrf_exempt
def allot(request):
    if request.method=='POST':
        name=request.POST.get('name')
        sub=request.POST.get('sub')
        grade=request.POST.get('class')
        status='You have been alloted Godparent to '
        prelim=submatch.Matchmaker(grade,sub)
        if not prelim:
            status='You are on the Waitlist.<br>'
            
            STATUS=waitlist.wl(name,grade,sub)
            
        else:
            STATUS=str(prelim)
            update.update_subject(prelim,name)
            
            
        about='''<html>
                {%load static%}
        
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        body {
          font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
         
        }
        
        * {
          box-sizing: border-box;
        }
        
        .container {
          padding: 16px;
          background-color: rgb(19, 162, 228);
          background-image: url("{% static 'Images/yay.png'%}");
          height: 1000px; 
          background-position: center;
          background-repeat: no-repeat; 
          background-size: cover;
          text-align: center;
          align-items: center;
          
        }
        .container3 { 
          height: 200px;
          position: relative;
          border: 3px solid green; 
        }
        
        .center {
          margin: 0;
          position: absolute;
          top: 50%;
          left: 50%;
          -ms-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
        }
        
        hr {
          border: 1px solid #141111;
          margin-bottom: 30px;
        }
        
       
        </style>
        </head>
        <body>
        
       
        <br>
        
        <form method = 'POST'>
        
            <div class="container">
               
                <h1 style="font-size: 50px; font-family:Verdana; color:rgb(7, 7, 7);"><b>THANK YOU!</b></h1><br>
                 <br>      <h2 style="font-size: 40px; color: #130e12;">Your Status is : '''+status+STATUS+'''
            <br><br>
            </h2></div>
                </body>
                </html>'''
     
            
        django_engine=engines['django']
        template=django_engine.from_string(about)
        html=template.render()
        return HttpResponse(html) 
   