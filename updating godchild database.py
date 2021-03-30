# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:37:05 2021

@author: anisumitaya
"""
import mysql.connector
db=mysql.connector.connect(host='localhost',user='Sristi',passwd='Welcome',database='DaddyLongLegs')
cursor=db.cursor()

'''this function updates the value of health/edu, overhead and finaid columns
in the database to 0 after the child has been assigned to a sponsor.
preference argument of this function is the preference chosen by sponsor.
blist argument is the return value of the healthedufunc or overheadfunc or 
finaidfunc'''

#########################################################
preference='overhead'
budget=2000                        ####To be retrieved from user through form.
############################################################
import Money

List=Money.money(preference,budget)  

def update_godchild_table(preference, blist):
    if preference =="health/edu":
        for j in blist:
            string1= "update gcinfo set health_edu = 0 where name ='{}'".format(j)
            cursor.execute(string1)
            db.commit()
    elif preference =="overhead":
        for j in blist:
            string2= "update gcinfo set overhead_ex = 0 where name ='{}'".format(j)
            cursor.execute(string2)
            db.commit()
    elif preference == "finaid":
        for j in blist:
            string3= "update gcinfo set health_edu = 0 where name ='{}'".format(j)
            string4= "update gcinfo set overhead_ex = 0 where name ='{}'".format(j)
            string5= "update gcinfo set finaid = 0 where name ='{}'".format(j)
            cursor.execute(string3)
            db.commit()
            cursor.execute(string4)
            db.commit()
            cursor.execute(string5)
            db.commit()

update_godchild_table(preference,List)

def ValueforDjango():
    return List       