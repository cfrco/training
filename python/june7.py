#!/usr/bin/env python

def pem(s,o,i,l):
    if l == i: # find pem
        print o

    else :
        for c in s: # run all char in string
            o = o[:i]   # now index is i ,you don't care o[i:]
            if not c in o: # if c is in o,so s can be put into o[i]
                o = o+c
                pem(s,o,i+1,l) #find next
            
while True:
    instr = raw_input("enter>>")
    for i in range(1,len(instr)+1):
        pem(instr,"",0,i)
        print "============="
