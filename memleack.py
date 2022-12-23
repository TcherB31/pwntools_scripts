#!/usr/bin/env python3
import pwntools pwn
from pwn import *
import sys

binary = ELF(sys.argv[1])
p = process(binary.path) 

while True:

    data = os.urandom(1024)  

    p.sendlineafter(data, '\n')

    valgrind_output = p.recvall()

    if 'definitely lost' in valgrind_output: 
        print('Memory Leak Detected!')
      
        break 
