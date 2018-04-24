# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 15:32:50 2018

@author: rajashekhar
"""

class stl:
    
    def str1(self,a):
        b=""
        i=0
      
        k=len(a)-1
        print(k)
        while k>=0:
            if (a[i]>='a' and a[i]<='z') or (a[i]>='A' and a[i]<='Z') or (a[i]==" "):
                b=a[i]+b
                k-=1
                i+=1
        print(b)
        print(len(b))
        print(len(a))
        t=0
        r=0
        w=len(a)-1
        p=len(b)
        #y=True
        
        while w>=0:
            if (a[t]>='a' and a[t]<='z') or (a[t]>='A' and a[t]<='Z') or (a[t]>='0' and a[t]<='9'):
                if a[t].lower()==b[r].lower():
                    r=r+1
                    print(b[r])
                #elif a[t]!=b[r]:
                    
                 #   x+=0
                  #  break
            t+=1
            w-=1
        print(r)
        print(p)
        
        if r!=p:
            print("not pallindrone")
        else:
            print("pallindrone")
             
                    
                
            
            
            
        
ob=stl()
ob.str1("A man, a plan, a canal: Panama")
#ob.str1("nitin")



        
        
    