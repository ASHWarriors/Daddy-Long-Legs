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
#import Money                     ####To be retrieved from user through form.
############################################################


def update_godchild_table(preference, blist):
    if preference =="health/edu":
        for j in blist:
            string1a= "update gcinfo set finaid = finaid- health_edu where name ='{}'".format(j)
            cursor.execute(string1a)
            db.commit()
            string1b= "update gcinfo set health_edu = 0 where name ='{}'".format(j)
            cursor.execute(string1b)
            db.commit()
    elif preference =="overhead_ex":
        for j in blist:
            string2a= "update gcinfo set finaid = finaid- overhead_ex where name ='{}'".format(j)
            cursor.execute(string2a) 
            db.commit()
            string2b= "update gcinfo set overhead_ex = 0 where name ='{}'".format(j)
            cursor.execute(string2b)
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
            
