# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 15:05:13 2018

@author: rajashekhar
"""

class Generator:
    def cal(self):
        a,b=0,1
        while True:
            
            yield a
            a,b=b,a+b
        
    
        
ob=Generator()
for f in ob.cal():
        if f>100:
            break
        print (f)
#ob.cal()

        