# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 14:41:00 2018

@author: rajashekhar
"""

"""
in remote system we have to type

sudo netcat -l 999
and password of that system
output:
hi bangalore message is printed in remote system  

"""




#!user/bin/python
import telnetlib
host="localhost"
tn=telnetlib.Telnet(host,"999")
tn.write("hi bangalore\n")
print tn.read_all()
