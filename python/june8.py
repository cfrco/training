#!/usr/bin/env python

def pem(s):
    sl = {}

    for c in s:
        if c in sl :
            sl[c] += 1
        else :
            sl[c] = 1

    _pem(s,sl,"",0)

def _pem(s,sl,o,i):
    if len(s) == i:
        print o
    else :
        for c in sl:
            if sl[c] > 0 :
                sl[c] -= 1
                o = o[:i]+c
                _pem(s,sl,o,i+1)
                sl[c] += 1


while True:
    instr = raw_input("enter>>")
    pem(instr)
