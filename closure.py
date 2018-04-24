# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 09:55:15 2018

@author: rajashekhar
"""

def outer(msg):
    hi=msg
    def inner():
        print(hi)
    return inner()
one=outer("bangalore")
