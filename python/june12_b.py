#!/usr/bin/env python

def i2b(i): #int to bin
    """
        Ex i2b(10) = [Ture,False,True,False]
    """

    out = []

    while i > 0 :
        out.insert(0,i%2==1)
        i /= 2

    return out


def fix_len(b,l):
    """
        b = [T,F,T]
        l = 5
        fix_len(b,l) 
        b = [F,F,T,F,T]
    """

    while len(b) < l :
        b.insert(0,False)

    return b


def subset(s):
    l = len(s)

    for i in range(0,2**l):
        b = fix_len(i2b(i),l)

        o = ""
        for j in range(0,l):
            if b[j] :
                o += s[j]
        print o

while True :
    instr = raw_input(">>>")
    subset(instr)
