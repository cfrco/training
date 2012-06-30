#!/usr/bin/env python

def com(s,l):
    table = {}
    
    for c in s:
        if c in table:
            table[c] += 1
        else :
            table[c] = 1

    _com(table,"",l,0)

def _com(t,o,l,i):

    # out
    if i == l :
        print o
        return 
    """ 
     because it is combination,we don't care the order.
     we only deal chars that after the last dealed char.
     Example :
     a:2 ,b :1,c:1
     >> com(table,3) 
     now -> ab?
     we don't care `a` because it was dealed.
     we only chose `b` or `c` ,but now b:0,
     final -> abc
    """

    # use for find the last dealed char
    b = False
    if len(o) > 0 :
        last_c = o[-1]
    else :
        b = True
    
    for c in t:
        if b==False and last_c==c : # find
            b = True
        
        if b and t[c] > 0: # if find
            t[c] -= 1
            o = o[:i]+c
            _com(t,o,l,i+1)
            t[c] += 1
            
while True :
    instr = raw_input(">>>")
    n = int(raw_input("(number)>>"))
    com(instr,n)
