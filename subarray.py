# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 17:40:45 2018

@author: rajashekhar
"""

class lis:
    def lis1(self,l):
        k=[]
        summ=l[0]
        z=len(l)-1
        p=z
        i=0
        j=0
        while z>=0:
            while p>=0:
                if summ < l[i]+l[j]:
                    k=l[i]+l[j]
                   # k.extends(l[j])
                    summ=l[i]+l[j]
                p=p-1
                j=j+1
            z=z-1
            
        print(summ)
        
ob=lis()
v=[9,1,1]
ob.lis1(v)
            
            
        