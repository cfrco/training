#!/usr/bin/env python

l2s = [(4.0,"A+"),(4.0,"A"),(3.7,"A-"),(3.3,"B+"),(3.0,"B"),(2.7,"B-"),
       (2.3,"C+"),(2.0,"C"),(1.7,"C-"),(1.0,"D"),(0.0,"E")]

def getScore(level):
    for ls in l2s:
        if level == ls[1]:
            return ls[0]
    return 0.0

def get_s(line):
    o = line.split(" ")
    if o[0] == "-1":
        return (None,None)
    return (int(o[0]),int(o[0])*getScore(o[1]))

def load_score_table(filename):
    out = []
    for line in open(filename,"r"):
        k = line.split(" ")

        for i in range(0,len(k),2):
            out += [(float(k[i]),float(k[i+1]))]
    
    return out

s = 0
cc = 0
while True:
    line = raw_input()
    c,sc = get_s(line)
    
    if sc == None:
        break

    s += sc
    cc += c

avg = s/cc
avg = int(avg*100)/100.0
print "Sum:",s
print "Average:",avg

sal = load_score_table("scoretable")
sal = sorted(sal,key = lambda s:s[1],reverse=True)

for i in range(0,len(sal)-1):
    if avg == sal[i][1]:
        print "Score:",sal[i][0]
        break
