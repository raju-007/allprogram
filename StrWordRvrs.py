# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 10:03:27 2018

@author: rajashekhar
"""

class Reverse:
    def rev(self,string):
        strrev=""
        
        for rec in string.split(" "):
            
            strrev=rec+" "+strrev
            
        print(strrev)
    
ob=Reverse()
file=open("StrWordRvrs.txt","r")
r=file.readlines()
p=""
print(r)
for j in r:
    p=j
    ob.rev(p)


"""
te=open("ban.txt","r+")
ka=te.readlines()            
print(ka)      
ob=stl()
for n in ka:
    ob.str1(n)
"""