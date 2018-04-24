# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 09:31:38 2018

@author: rajashekhar
"""
"""
 max_so_far = 0
    max_ending_here = 0

Loop for each element of the array
   max_ending_here = max_ending_here + a[i]
   if(max_ending_here < 0)
            max_ending_here = 0
   if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
return max_so_far

"""


class SubArray:
     def arr(self,a):
        
        max_so_far = 0
        max_ending_here = 0
        max_ending_here = max_ending_here + a[i]
     if max_ending_here < 0:
            max_ending_here = 0
     if max_so_far < max_ending_here :
            max_so_far = max_ending_here
            print(max_so_for)
#return (max_so_far)
        
ob=SubArray()
lis = [2,1,-3,4,-1,2,1,-5,4]       
ob.arr(lis)
 
        