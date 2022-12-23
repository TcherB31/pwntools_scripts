#!/usr/bin/env python
import pwntools pwn
from pwn import *
import sys
 
binary = ELF(sys.argv[1])
 
p = process(binary.path, env={"LD_PRELOAD": "libc-2.23.so"}) 
 
def generateRandomData():
    
    randomData = ""                              
    for _ in range(0, 1024):                      
        randomData += chr(random.randint(0x00, 0xff))  
    return randomData                           
 while True:                                 
    try:                                       
        pwnInput = generateRandomData()              
        log.info("Sending %d bytes of fuzzing input..." % len(pwnInput))     
        p.sendlineafter('>', pwnInput)          
        p.recvuntil('\n') 
                                  
    except EOFError:                                
        log.info("Program crashed!")             
