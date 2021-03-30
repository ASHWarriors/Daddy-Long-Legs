# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 13:23:20 2021

@author: Sristi
"""

def upgodp(data):
    import mysql.connector
    db=mysql.connector.connect(host='localhost',user='Sristi',passwd='Welcome',database='DaddyLongLegs')
    cursor=db.cursor()
    s="insert into godparents values('{}','{}','{}');".format(data[0],data[1],data[2])
    cursor.execute(s)
    db.commit()
    
    