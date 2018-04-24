# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 14:23:54 2018

@author: rajashekhar
"""

import socket
def td():
    host="192.168.1.155"
    port=5000
    s=socket.socket()
    s.bind((host,port))
    s.listen(1)
    c,addr=s.accept()
    print ("connection from :" +str(addr))
    while True:
        data=c.recv(1024)
        if not data:
            break
        print("from connected user: "+str(data))
        data=str(data).upper()
        print("sending: " +str(data))
        c.send(data)
    c.close()

td()

    