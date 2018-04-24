# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 10:04:10 2018

@author: rajashekhar
"""

class ite:
    def __init__(self):
        self.index=-1
        self.cha=["hbo","cnn","public"]
    def __iter__(self):
        return (self)
    def __next__(self):
        self.index+=1
        if self.index==len(self.cha):
            raise StopIteration
        return (self.cha[self.index])
        
ob=ite()
i=iter(ob)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
        