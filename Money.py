# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:34:19 2021

@author: anisumitaya
"""
'''this child_data is a list of tuples. I made this because i dont have pymysql. 
please replace this example list with fetchall function to get a list of tuples of
various rows of the godchild table'''

# =============================================================================
# child_data= [('name1', '0 to 2', 0, 423400, 499200), 
#              ('name2', '8 to 13', 339025, 0, 1211025),
#              ('name3', '13 to 18', 277898, 1141000, 1418898),
#              ('s', '3 to 8', 540775, 621995, 1162770),
#              ('name5', '2 to 3', 74000, 243000, 317000),
#              ('name6', '3 to 8', 540775, 621995, 1162770),
#              ('name7', '3 to 8', 540775, 621995, 1162770),
#              ('name8', '8 to 13', 339025, 872000, 1211025),
#              ('name9', '2 to 3', 0, 0, 0),
#              ('name10', '13 to 18', 277898, 1141000, 1418898),]
# =============================================================================

############The Fetchall Function ##########################################

def child_data():
    import mysql.connector
    db=mysql.connector.connect(host='localhost',user='Sristi',passwd='Welcome',database='DaddyLongLegs')
    cursor=db.cursor()
    cursor.execute("Select * from gcinfo")
    child_data=cursor.fetchall()
    return child_data
#print(child_data())
###########################################################################

def sorting(l):           
    ll=[]
    for i in l:
        if i[1]=='0 to 2':
            ll.append(i)
    for i in l:
        if i[1]=='2 to 3':
            ll.append(i)
    for i in l:
        if i[1]=='3 to 8':
            ll.append(i)
    for i in l:
        if i[1]=='8 to 13':
            ll.append(i)
    for i in l:
        if i[1]=='13 to 18':
            ll.append(i)
    return ll


#######################################################################
'''the following three functions return a list of name of the godchildren that
are eligible to be sponsored by the sponsor according to his/her budget'''
'''if sponsor selects health/education then use healthedufunc
if sponsor selects overhead expenses then use overheadfunc
if sponsor selects financial aid then use finaidfunc'''

def healthedufunc(money,alist):
    #cdata=child_data()
    res=[]
    tot=0
    for t in alist:
        if t[2] !=0:
            tot+=t[2]
            if tot<= money:
                res.append(t[0])
            else:
                break
        else:
            pass
    return res

def overheadfunc(money,alist):
    #cdata=child_data()
    res=[]
    tot=0
    for t in alist:
        if t[3] !=0:
            tot+=t[3]
            if tot<= money:
                res.append(t[0])            #EXCEPTIONAL HANDLING 1:
                                       #WHAT IF MONEY LEFT IN BUDGET STILL? INFORM USER
            else:
                break
        else:
            pass
    return res

def finaidfunc(money,alist):
    #cdata=child_data()
    res=[]                             #EXCEPTIONAL HANDLING 2:
    tot=0                   #WHAT IF BUDGET DOESN'T MEET THE MINIMUM EXPENSE?
    for t in alist:         # CONTRIBUTION TO BE STILL MADE!!!!!
        if t[4] !=0:
            tot+=t[4]
            if tot<= money:
                res.append(t[0])
            else:
                break
        else:
            pass
    return res
############################################################################

child_data()
sorted_child_data= sorting(child_data()) #this returns a list of tuples which are 
                                             #sorted according to age group

####################A Sweet Function that returns what's asked################
def money(need,budget): 
    sorted_child_data= sorting(child_data())    
    if need=="health/edu":                        
        return healthedufunc(budget, sorted_child_data)
    elif need=="overhead_ex":
        return overheadfunc(budget,sorted_child_data)
    else:
        return finaidfunc(budget,sorted_child_data) 
    
#===============================================================================#    
def sortdata():
    sorted_child_data= sorting(child_data())
    return sorted_child_data
    
#print(sorted_child_data)
#print(finaidfunc(2600000,sorted_child_data)) 
#print(overheadfunc(1000000,sorted_child_data))
#print(healthedufunc(200000, sorted_child_data)) 

'''the above three print functions are just some test cases run by me
the money argument of each function will be the budget mentioned by sponsor
and the alist argument of each function will always be sorted_child_list '''
