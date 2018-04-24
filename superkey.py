# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 17:41:24 2018

@author: rajashekhar
"""

class b:
    def disp(self):
        print("hello boys")
class c(b):
    def disp(self):
        super().disp()
        print("hello girl")
ob=c()
ob.disp()
