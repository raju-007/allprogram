# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:16:07 2018

@author: rajashekhar
"""
import textwrap

def me(z):
    k=""
    ls=textwrap.wrap(z,4)    
    for i in range(len(ls)):
        k+=ls[i] + '\n'
    return k
   
           
        
k="abcdefghijklmnopqrstuvwxyz"
print(me(k))