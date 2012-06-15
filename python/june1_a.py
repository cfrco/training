#!/usr/bin/env python

fp = open("june1_a.out","w+")

a = 1
b = 1

fp.write(str(a)+'\n')
fp.write(str(b)+'\n')

for i in range(0,1000):
    fp.write(str(a+b)+'\n')
    a,b = (b,a+b) # you should try this

fp.close()
