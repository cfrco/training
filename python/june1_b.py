#!/usr/bin/env python

fp = open("june1_b.out","w+")

fib = [1,1]

for i in range(2,1000):
    fib += [fib[i-1]+fib[i-2]]

for f in fib:
    fp.write(str(f)+'\n')

fp.close()
