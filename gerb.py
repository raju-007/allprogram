# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 10:38:52 2018

@author: rajashekhar
"""
import time
def remote():
    yield "abc"
    yield "ahfoah"
itr=remote()
#iter
start=time.time()

print(next(itr))
end=time.time()
print((end-start)*1000)