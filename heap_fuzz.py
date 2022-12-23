#!/usr/bin/env python3
import pwntools pwn
from pwn import *

target = '<YOUR TARGET>'
port = <PORT> 
context.arch = 'amd64'
binary_path = '<PATH TO BINARY>'
libc_path = '<PATH TO LIBC>'

conn = remote(target, port) 
debugger = gdb.debug(binary_path, gdbscript='set follow-fork-mode child')
 
payload_size = <SIZE OF PAYLOAD> # Size of payload in bytes (e.g., 0x1000)            
         buf= ''   for x in range(payload_size): buf += chr(random.randint(0,255)) conn.sendline(buf)
         retcode= conn.recv() if retcode == -11: print("Program crashed") else: print("Program did not crash")
