#!/usr/bin/env python3
import pwntools pwn
from pwn import *
import sys

input_data = input("Please enter the input data: ")

elf = pwntools.ELF('./myBinary')
rop = pwntools.ROP(elf)
rop.raw(input_data)
 
    print("Exploit generated successfully!")
