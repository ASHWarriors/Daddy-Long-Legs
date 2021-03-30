# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 19:24:57 2021

@author: anisumitaya
"""


def wl(name,grade,sub):
    import mysql.connector
    db=mysql.connector.connect(host='localhost',user='Sristi',passwd='Welcome',database='Daddylonglegs')
    cursor=db.cursor()
    
    waiting= "select * from child_sub where patron= 'NULL';"
    cursor.execute(waiting)
    waitlist= cursor.fetchall()
    print(waitlist)
    if waitlist==[]:
        val= "insert into patron values ('{}','{}','{}');".format(name,grade,sub)
        cursor.execute(val)
        db.commit()
        to_print=''
    else:
        to_print='Please select a subject choice and grade from the following:<br>'
       
        for i in waitlist:
            stemp=i[1]+' '+i[2]+'<br>'
            print(stemp)              #i=(name,grade,sub)
            to_print+=stemp
    return to_print
            
            
            
            
            
'''for j in i:
                stemp +=j+"<br>"
to_print += stemp 
return to_print'''
