# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:01:33 2021

@author: anisumitaya
"""
# our child_sub is equal to fetchall of child_sub table in the database which will
# have columns: name, grade, subject. this will be a list of tuples.
child_sub= [("name1", "3", "math"),
            ("name2", "5", "history"),
            ("name3", "2", "english"),
            ("name4", "5", "history")]
list_1=[]
for i in child_sub:
    list_1.append(i[1]+i[2]) 
    
'''input of sub_match will be prefrred grade and subject of sponsor'''
def sub_match(grade, subject):
    s= grade+subject
    res=[]
    for i in range(len(list_1)):
        if s==list_1[i]:
            res.append(child_sub[i][0])
    if len(res)==0:
        p="no children were matched"
    else:
        p=""
        for i in res:
            p+= " "+i
    return p

#print(sub_match("5", "history"))  