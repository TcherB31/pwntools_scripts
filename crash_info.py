#!/usr/bin/env python
import pwntools pwn
from pwn import * 
import sys 

binary = "x86_64_binary" 
target = process(binary) 

pattern = cyclic(100)  

target.sendline(pattern)  
  
crash_info = target.recvall()  

vulnerability_type = analyze_crash(crash_info)  

if vulnerability_type == "high":                   exploit(target, binary, crash_info)
