#!/usr/bin/env python

fp = open("june1_c.out","w+")

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else :
        return fib(n-1)+fib(n-2)

for i in range(1,31):
    fp.write(str(fib(i))'\n')

fp.close()
