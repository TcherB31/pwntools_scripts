#!/usr/bin/env python3
import pwntools pwn
from pwn import *

target = remote('<server_ip>', <port>)
fuzz_string = 'A' * 1024 
target.send(fuzz_string)
response = target.recv()

if 'Segmentation fault' in response: 
    print('The application has crashed due to fuzzing!')
