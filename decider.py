# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 00:36:40 2021

@author: anisumitaya
"""
from DaddyLongLegs import upgcinfo
from DaddyLongLegs import Money
from DaddyLongLegs import webparsing
from DaddyLongLegs import surplus_funds

def output(preference, money, some_list):
    if preference=="health/edu":
        l= Money.healthedufunc(money,some_list)
        if l==[]:
            out= "insufficient funds"
        else:
            out = l
    elif preference=="overhead_ex":
        l= Money.overheadfunc(money,some_list)
        if l==[]:
            out= "insufficient funds"
        else:
            out = l
    elif preference=="finaid":
        l=Money.finaidfunc(money,some_list)
        if l==[]:
            out= "insufficient funds"
        else:
            out = l 
            
    return out 