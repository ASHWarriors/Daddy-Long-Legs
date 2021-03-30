# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:20:16 2021

@author: anisumitaya
"""

from DaddyLongLegs import upgcinfo
from DaddyLongLegs import Money
from DaddyLongLegs import webparsing
from DaddyLongLegs import surplus_funds

#rom surplus_funds import *


def surplus(budget, clist, preference):
    total=0
    result=budget
    cdata=Money.child_data()
    print(cdata)
    print(clist)
    for i in clist:
        for j in range(len(cdata)):
            if i== cdata[j][0]:
                ind=j
               # result=0
                #break
        if preference=="health/edu":
            total += cdata[ind][2]
        elif preference=="overhead_ex":
            total += cdata[ind][3]
        elif preference =="finaid":
            total += cdata[ind][4] 
           # print(total,'ln30')
        else:
            #print(total,'ln32')
            pass
        #print(total,'ln34')
        result = budget-total
    print(total)
    return result 

'''
def surplus(budget, clist, preference):
   #import Money
    cdata=Money.child_data()
   #sorted_child_data=sortdata()
   #print(cdata)
    total=0
    for i in clist:
        for j in range(len(cdata)):
            if i== cdata[j][0]:
                ind=j
               # break
                if preference=="health/edu":
                    total += cdata[ind][2]
                elif preference=="overhead_ex":
                   #print( cdata[ind][3])
                    total +=  cdata[ind][3]
                   #print(total)
                elif preference =="finaid":
                    total += cdata[ind][4] 
                else:
                    pass
    print(total)
    result = budget-total
    return result '''
# the above function calculates surplus amount for both cases, when budget is too
# high or budget is too low
'''for the above function, budget= budget of sponsor
clist= list of names returned by healthedufunc/overheadfunc/finaidfunc
preference= preference entered by sponsor'''
#print(surplus(1000,overheadfunc(1000, sorted_child_data),"overhead"))  
#mport Money
#rom Money import *
def BankKnows(budget,preference):
    sorted_child_data=Money.sortdata()
    
    import mysql.connector
    db=mysql.connector.connect(host='localhost',user='Sristi',passwd='Welcome',database='bank_surplus')
    cursor=db.cursor()
    cursor.execute("select * from bank")
    paisa= cursor.fetchall()
    #print(paisa[-1][0])
    if preference=='overhead_ex':
        splus=surplus(budget,Money.overheadfunc(budget, sorted_child_data),preference)
        current_surplus= paisa[-1][0] #+ splus
        new_surplus= current_surplus+splus
    elif preference=='health/edu':
         splus=surplus(budget,Money.healthedufunc(budget, sorted_child_data),preference)
         current_surplus= paisa[-1][0] #+ splus
         new_surplus= current_surplus+splus
    else:
        splus=surplus(budget,Money.finaidfunc(budget, sorted_child_data),preference)
        current_surplus= paisa[-1][0] #+ splus
        new_surplus= current_surplus+splus
        
    #print(new_surplus)
    s=cursor.execute("insert into bank values({})".format(new_surplus))
    db.commit()
    return new_surplus,splus



