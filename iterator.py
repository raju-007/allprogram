# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 15:33:00 2018

@author: rajashekhar
"""

class Channel:
    def __init__(self):
        self.cha=["hbo","cnn","public"]
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index == len(self.cha):
            raise Exception
        return self.cha[self.index]
ob=Channel()
itr=iter(ob)
print(next(itr))