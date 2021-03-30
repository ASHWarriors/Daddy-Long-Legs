# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:56:53 2021

@author: anisumitaya
"""


def update_subject(dlist,name):
    import mysql.connector
    db=mysql.connector.connect(host='localhost',user='Sristi',passwd='Welcome',database='DaddyLongLegs')
    cursor=db.cursor()
    for i in dlist:
        s= "update child_sub set subject='NULL', patron='"+name+"' where name='{}';".format(i)
        cursor.execute(s)
        db.commit() 
        
        