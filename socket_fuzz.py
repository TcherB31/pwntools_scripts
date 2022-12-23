#!/usr/bin/env python3
import pwntools pwn
from pwn import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
port = 443
  
s.connect(('localhost', port)) 

buffer = b'A' * 1024

while len(buffer) <= 1000:   

    try:                                 
        s.send(buffer) 
        s.recv(1024)                    
        print("Sent %s" % repr(buffer))  
        buffer = buffer + b'A' * 1024  

    except:                              
        print("Buffer length exceeded")  
        break
