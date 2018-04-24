# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 16:59:37 2018

@author: rajashekhar
"""

class primeno:
    def palli(self):
        n=9
        m=n/2
        flag=1
        if n==0 or n==1:
            print("not prime")
        else:
            i=2
            while i<=m:
                if n%i==0:
                    print("not prime")
                    flag=0
                    i=i+1
                    break
                else:
                    i=i+1
                
                
        if flag==1:
            print("prime")
            
ob=primeno()
ob.palli()                    