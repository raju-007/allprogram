# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 15:01:11 2018

@author: rajashekhar
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
def time_in(func):
    def wrapper(*args,**kargs):
        start=time.time()
        result=func(*args,**kargs)
        end=time.time()
        print(str((end-start)*1000))
        return result
    return wrapper



@time_in
def sqr(num):
    result=[]
    for n in num:
        result.append(n*n)
    return result
array=range(0,1000000)
ob=sqr(array)

    

