# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 09:50:53 2018

@author: rajashekhar
"""

def maxSubArray(ls):
    lk=[]
    if len(ls) == 0:
       raise Exception("Array empty") 
      
    ru = mx = ls[0]
    i = 0
    start = finish = 0

    for j in range(1, len(ls)):
        if ls[j] >=(ru + ls[j]):
            ru = ls[j]
            
            i = j
            
        else:
            ru += ls[j]
            

        if ru> mx:
            
            mx = ru
            start = i
            finish = j

    print ("maxsum = ", mx)
    print ("start = ", start, "finish = ", finish)
    k=start
    while k<=finish:
        lk+=[ls[k]]
        k+=1
    print(lk)
    
maxSubArray([2,1,-3,4,-1,2,1,-5,4])
