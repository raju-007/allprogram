# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 17:43:41 2018

@author: rajashekhar
"""

class Exception_1:
    def div(self,a,b):
        c=1
        try:
            c=a/b
        except Exception as e:
            print(e)
            
ob=Exception_1()
ob.div(10,0)

            
    