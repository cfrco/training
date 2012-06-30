#!/usr/bin/env python

import june11

while True:
    instr = raw_input(">>>")
    
    print "" #empty 
    for i in range(1,len(instr)+1):
        june11.com(instr,i)

