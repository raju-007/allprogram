# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 14:31:15 2018

@author: rajashekhar
"""

import socket
def Main():
    host="localhost"
    port=5000
    s=socket.socket()
    s.connect((host,port))
    message=raw_input("->")
    while message != 'q':
        s.send(message)
        data=s.recv(1024)
        print("received from server :" +str(data))
        message=raw_input("->")
    s.close()
if __name__=="__main__":
    Main()
    