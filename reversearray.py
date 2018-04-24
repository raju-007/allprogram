# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 10:29:12 2018

@author: rajashekhar
"""

def fun(k):
    i=0
    j=len(k)-1
    while i<j:
        temp=k[i]
        temp2=k[j]
        k[i]=temp2
        k[j]=temp
        i+=1
        j-=1
    print(k)
#print("enter size of list")
lis=[]
z=int(input("enter the size of list"))
print("enter array elements")
for i in range(0,z):
    t=int(input("enter the number"))
    lis.append(t)
print(lis)
fun(lis)
    