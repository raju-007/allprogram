# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 16:21:22 2018

@author: rajashekhar
"""

import getpass
import sys
import telnetlib


host="localhost"
user=raw_input("enter usr name:")
password=getpass.getpass()
tn=telnetlib.Telnet(host)
tn.read_