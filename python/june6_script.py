#!/usr/bin/env python

from june6 import *

prototype = ["name","age","gender","education","dept"]
print prototype

table = create(prototype)
print table

entry = {"name":"cat","gender":"male","education":"ntust","dept":"csie","age":19}
print entry

print insert(table,entry)
print table

entry = {"name":"cat","gender":"male","education":"ntust","dept":"csie"}
print insert(table,entry) #False because no "age"
print table

for i in range(1,6):
    entry = {"name":"cat"+str(i),"gender":"male","education":"ntust","dept":"csie","age":15+i}
    insert(table,entry)

res = select(table)
for e in res :
    print e

entry = {"name":"dog","gender":"male","education":"ntu","dept":"csie","age":20}
insert(table,entry)
entry = {"name":"cfg","gender":"male","education":"ntust","dept":"csie","age":20}
insert(table,entry)

res = select(table,{"name":"dog"})
print res

res = select(table,{"education":"ntust"})
for e in res :
    print e

res = select(table,{"education":"ntust","age":19})
for e in res :
    print e

print update(table,{"education":"super_ntust"},{"education":"ntust"})
res = select(table)
for e in res :
    print e

print update(table,{"education":"ntust"},{"education":"super_ntust"})
res = select(table)
for e in res :
    print e

print update(table,{"education":"super_ntust"},{"education":"ntust","age":20})
res = select(table)
for e in res :
    print e

print delete(table,{"education":"super_ntust"})
res = select(table)
for e in res :
    print e

print delete(table,{"age":19,"name":"cat4"})
res = select(table)
for e in res :
    print e
