# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:40:50 2021

@author: Sristi
"""

#CONNECTIVITY MODULE-----AKA-----LIFE SAVER MODULE

from DaddyLongLegs import upgcinfo
from DaddyLongLegs import Money
from DaddyLongLegs import webparsing
from DaddyLongLegs import surplus_funds
#from gcinfo import *
#from Money import *
#from webparsing import *
# from suject_match import *
#from upgcinfo import *


# webpage of the sponsor - we get his details -- budget, name, email and preference
#Money function
#upgcinfo function
#inputs1=["overhead_ex",'5000000']

def IamGod(inputs1):
    global List
    global preference
    global budget
    from DaddyLongLegs import decider
    preference=inputs1[0]
    budget=float(inputs1[1])   
    List=Money.money(preference,budget)
    cdata=Money.sortdata()
    
   # print(List)    
    if decider.output(preference,budget,cdata)=="insufficient funds":
        msg='''No child has been alloted to you. This could be due to the following reasons:
        1) All the substantial needs of the children have been met.
    2) Your funds aren't sufficient to support the substantial needs of the child.'''
        #print(surplus_funds.surplus(float(budget), List, preference))
        #surplus_funds.BankKnows(float(budget),preference)
        return msg ,0
    
    else:
        #print(surplus_funds.surplus(float(budget), List, preference))
        #surplus_funds.BankKnows(float(budget),preference)
        return str(List),1

'''
def collect():
            
'''        
#child_data=child_data()
#sorted_child_data=sortdata()        

#print(IamGod(inputs1))



##################################################################################

#For God Child Details Page
'''
inputs2=['Cami','17'] #To be entered by user on web app
Name="'"+inputs2[0]+"'"
Age=int(inputs2[1]) #To be entered by user on web app
'''

#This part allots correct age-group to the child and formats data to be fed into the database

age_grp,col_healthedu,overhead,fin_aid = webparsing.data()
def entry(inputs2):
    Name="'"+inputs2[0]+"'"
    Age=int(inputs2[1])    
    email=inputs2[2]
    rgid=inputs2[3]
    if Age in range(0,2):
        age="'"+age_grp[0]+"'"
        Health_edu=col_healthedu[0]
        Overhead_Ex=overhead[0]
        Finaid=fin_aid[0]
    elif Age in range(2,3):
       age="'"+age_grp[1]+"'"
       Health_edu=col_healthedu[1]
       Overhead_Ex=overhead[1]
       Finaid=fin_aid[1]
    elif Age in range(3,8):
        age="'"+age_grp[2]+"'"
        Health_edu=col_healthedu[2]
        Overhead_Ex=overhead[2]
        Finaid=fin_aid[2]
    elif Age in range(8,13):
        age="'"+age_grp[3]+"'"
        Health_edu=col_healthedu[3]
        Overhead_Ex=overhead[3]
        Finaid=fin_aid[3]
    elif Age in range(13,19):
        age="'"+age_grp[4]+"'"
        Health_edu=col_healthedu[4]
        Overhead_Ex=overhead[4]
        Finaid=fin_aid[4]
   # else:
        #print("Invalid") #doesn't belong to any age group
    Info=[Name,age, str(Health_edu),str(Overhead_Ex),str(Finaid),"'"+email+"'","'"+rgid+"'"]
    return Info

#entry()
def rgid_col(alloted_kids,rgid):
     import mysql.connector
     db=mysql.connector.connect(host='localhost',user='Sristi',passwd='Welcome',database='Daddylonglegs')
     cursor=db.cursor()
     print(type(alloted_kids))
     for i in alloted_kids:
        query = "update gcinfo set patron_rg ='{}' where name = '{}';". format (rgid,i)
        cursor.execute(query)
        db.commit()
        
        
def IamChild(child1,child2):
    from DaddyLongLegs import dbchild
    dbchild.updation(child1)
    dbchild.upsub(child2)
    
#IamChild(inputs2)
###########################################################################################
