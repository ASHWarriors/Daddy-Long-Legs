# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 13:31:34 2021

@author: Sristi
"""






def uniqid():
    import math
    Pi=math.pi
    USE=Pi-3
    USE=str(USE)
    L=len(USE)
    Use=float(USE)*(L-1)
    Use=str(Use)
    global NEED
    NEED=USE[2:18]+Use[2:18]#Made a non recurring series with the help of pi :)
    NEED=int(NEED)
    NEED=NEED*NEED#EXTENDING THE DIGITS...
    NEED=str(NEED)
    
    import mysql.connector
    db=mysql.connector.connect(host='localhost',user='Sristi',passwd='Welcome',database='DaddyLongLegs')
    cursor=db.cursor()
    s="select count(patron_rg) from gcinfo where patron_rg!='NULL';"
   # print(NEED)
    cursor.execute(s)
    filled=cursor.fetchall()
    #print(filled[0][0])
    inn=filled[0][0]
    global ID
    ID=''
    for i in range(len(NEED)):
        ind=i
        #print(NEED,ID)
        if ind==inn*2 or inn==0:
            ID=ID+NEED[i]+NEED[i+1]#+NEED[i+2]+NEED[i+3]  #FIRST 2 DIGITS TAKEN
            #print(ID)
            if len(ID)==4:
                break
  
    return ID
print(uniqid())