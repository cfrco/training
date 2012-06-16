#!/usr/bin/env python

s2l = [(90,"A+"),(85,"A"),(80,"A-"),(77,"B+"),(73,"B"),(70,"B-"),
       (67,"C+"),(63,"C"),(60,"C-"),(50,"D"),(0,"E")]

fp = open("june2.in","r")

def getLevel(score):
    for sl in s2l:
        if score >= sl[0]:
            return sl[1]
    return "ERROR SCROE"

for line in fp:
    score = float(line)
    print getLevel(score)

