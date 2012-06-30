#!/usr/bin/env python

def subset(s):
    l = len(s)

    for i in range(0,2**l):
        j = i
        o = ""
        for k in range(0,l):
            if j%2 == 1:
                o += s[k]
            j /= 2
        print o

while True :
    instr = raw_input(">>>")
    subset(instr)
