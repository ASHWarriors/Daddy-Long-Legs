# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 02:20:48 2021

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
from DaddyLongLegs import upgpinfo
from DaddyLongLegs import unique




@csrf_exempt
def success(request):
    if request.method=='POST':
        global name
        global budget
        global preference
        name=request.POST.get('name')
        budget=request.POST.get('budget')
        preference=request.POST.get('preference')
        email=request.POST.get('email')
        f=open('buffer.txt','w')
        f.writelines([name+'\n',budget+'\n',preference+'\n'])
        f.close()
        
        print(budget,preference)
        from DaddyLongLegs import MASTER
        status='You have been alloted Godparent to '
        STATUS,F= MASTER.IamGod([preference,float(budget)])
        print(F)
        if F==0:
            status=''
            funds=budget
        else:
            print(STATUS)
            rgid=unique.uniqid()
            print(rgid)
            status=status+str(STATUS)+'<br> Your unique id is : '+rgid+'<br>Please remember this for login.'
            mn=Money.money(preference,float(budget))
            funds=str(surplus_funds.surplus(float(budget),mn, preference))
            upgpinfo.upgodp([rgid,name,email])
            upgcinfo.update_godchild_table(preference,mn)
            MASTER.rgid_col(mn,rgid)
        print(funds)

        
        about='''
        <html>
        {% load static %}
        

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
   background-image: url("{% static 'Images/yay.png'%}");
  background-size: cover;
  height: 600px; 
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
input[type=text] {
  width: 50%;
  padding: 15px;
  margin: 5px 0 20px 0;
  display: inline-block;
  border: 5;
  background: #faf9f9;
}

input[type=text]:focus {
  background-color: rgb(97, 125, 138);
  outline-style: double;
}

hr {
  border: 1px solid #141111;
  margin-bottom: 30px;
}

a {
  color: rgb(88, 100, 112);
}

#button4{
    width: 200px;
    height: 30px;
    color: rgb(12, 12, 17);
    background-color: rgb(11, 241, 42);
}
.signupbtn {
  float: left;
  width: 50%;
}
</style>
</head>
<body>

<br>

<form method = 'POST'>

    <div class="container">
       
        
        <div class ="center">
        <h1><b>THANK YOU!</b></h1><br>
        <p> '''+status+''' <br><br>
            Your surplus funds are '''+funds+'''<br>
        Would you like to store your funds in the Bank?</p>
        <button type="submit" class="btn" id="button4" formaction="/GP/info/collection/finaldonationpage"><b>YES</b></button>
        </form>
        <button id="button4"><b><a href='http://127.0.0.1:8000'>NO</b></button></a>
        
       
        </div>
    </div>
<br><br>


</body>
</html>
'''
        django_engine=engines['django']
        template=django_engine.from_string(about)
        html=template.render()
        return HttpResponse(html) 
   
    