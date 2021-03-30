# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:30:20 2021

@author: Sristi
"""

#Function 1---------------------------------------------------------------------
#######################To update table having GodChild Info####################

#import MASTER
#entry=MASTER.entry() #Get Data of the Child
#print(entry)
 #Format Data
#print(child)
def updation(child1):
    import mysql.connector
    db=mysql.connector.connect(host='localhost',user='Sristi',passwd='Welcome',database='DaddyLongLegs')
    cursor=db.cursor()
    cursor.execute("INSERT INTO gcinfo VALUES("+ child1 +");") #Insert into Table
    db.commit()
def upsub(child2):
    import mysql.connector
    #print(child2[0],child2[1],child2[2])
    string="INSERT INTO child_sub VALUES('{}','{}','{}','{}');".format(child2[0],child2[1],child2[2],'NULL')
    
    db=mysql.connector.connect(host='localhost',user='Sristi',passwd='Welcome',database='DaddyLongLegs')
    cursor=db.cursor()
    cursor.execute(string) #Insert into Table
    db.commit()

    