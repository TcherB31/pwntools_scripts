#!/usr/bin/env python3
import pwntools pwn
from pwn import *
import random
 
def fuzz(binary):
    
    proc = pwn.process(binary)
 
    rand_str = ''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(random.randint(10, 100))])
        
    proc.sendlineafter(rand_str)
        
    if "Segmentation fault" in proc.recvall():        
        print("[!] Segmentation fault detected!")    

    elif "Floating point exception" in proc.recvall():      
        print("[!] Floating point exception detected!")     

     else:                                                 
        print("[+] No crashes or exceptions found")     

 if __name__ == '__main__':      
     fuzz(sys.argv[1])
