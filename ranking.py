from z3 import *

L,B,J,M=Ints('Lisa Bob Jim Mary')
Bl,Bb,Bj,Bm=Bools('Bl Bb Bj Bm')

s=Solver()

#the rank is start from 1, and there are no same ranks
#Use this rules to make ranks be 1,2,3,4 separately
s.add(L+B+J+M==10,L>0,B>0,J>0,M>0,Not(L==B),Not(L==J),Not(L==M),Not(J==B),Not(M==B),Not(J==M))

s.add(And(Not(L==B+1),Not(L==B-1)))
s.add(Or(And(J==L-1,Bl),And(J==B-1,Bb),And(J==M-1,Bm)))
s.add(B==J-1)
s.add(Or(Bl,Bm),Not(And(Bl,Bm)))
s.add(Or(L==1,M==1))

print(s.check())
if s.check()==sat:
    print(s.model())

