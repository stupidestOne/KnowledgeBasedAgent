from z3 import *

s=Solver()

#If true: lady in this room; Else tiger in this room.
l1,l2,l3=Bools('l1 l2 l3')

s1=Not(l1)
s2=l2
s3=Not(l2)

s.add(If(s1,1,0)+If(s2,1,0)+If(s3,1,0)<=1)
s.add(If(l1,1,0)+If(l2,1,0)+If(l3,1,0)==1)

conclude=["lady in room 1","lady in room 2","lady in room 3"]
l=[l1,l2,l3]

for c in range(len(conclude)):
    s.push()
    s.add(Not(l[c]))
    if s.check()==unsat:
        print(s.check())
        print(conclude[c])
    s.pop()
