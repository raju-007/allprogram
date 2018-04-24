# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 14:04:46 2018

@author: rajashekhar
"""
"""
import getpass
import sys
import telnetlib
 
 
host="192.168.1.152"
user=input("enter ur telnet username: ")
password=getpass.getpass()
tn=telnetlib.Telnet(host)
tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")
tn.write("ls\n")
tn.write("exit\n")
print (tn.read_all())"""
import getpass
import sys
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls\n")
tn.write("exit\n")

print (tn.read_all())