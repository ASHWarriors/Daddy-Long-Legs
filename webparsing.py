# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 01:04:23 2021

@author: anisumitaya
"""
import urllib.request as url
import bs4 as bs

def clean(s):
    res=""
    for i in s:
        if i.isdigit()==1:
            res+=i
    return res 

source= url.urlopen('https://www.adityabirlacapital.com/abc-of-money/how-much-does-it-cost-to-raise-a-child-in-india').read()
soup=bs.BeautifulSoup(source,'lxml')
td= soup.find_all("td", {"style": "width: 85px;"})
indices=[15,16,26,28,29,35,37,38,39,46,48,56,58,66]
age_grp=["0 to 2","2 to 3","3 to 8","8 to 13","13 to 18"]  

biglist=[]
for j in indices:
    element =td[j].contents
    biglist.append(element)  
    
total=[]
for k in biglist:
    if len(k) >1:
        total.append(k)
        
final=[]
for z in total:
    nice= z[1]
    final.append(nice) 
    
list2=[]
for f in final:
    element2= f.contents
    list2.append(element2)  
    
fin_aid=[]
for t in list2:
    word=t[0]
    el=clean(word)
    fin_aid.append(int(el)//12)

health_edu=[]
for q in biglist:
    if len(q)==1:
        nice= clean(q[0])
        health_edu.append(int(nice)//12)  
col_healthedu=[health_edu[0]+health_edu[1], health_edu[2]+health_edu[3],health_edu[4]+health_edu[5]+health_edu[6],health_edu[7],health_edu[8]]

overhead=[]
for i in range(len(fin_aid)):
    oh= fin_aid[i]-col_healthedu[i]
    overhead.append(oh)  

###########################################################################
# This data function will return required info to GodChild Module    
def data():
    return age_grp,col_healthedu,overhead,fin_aid

# print("age groups are: ", age_grp)
# print("health/education cost is: ", col_healthedu) 
# print("overhead expenses are: ", overhead)  
# print("financial aid cost is: ", fin_aid) 