# KnowledgeBasedAgent

I used a mechanical theorem prover to solve problems by reasoning or finding models. 
To achieve it, I used Z3Prover, which is a high-performance theorem prover being developed at Microsoft Research.
The offical release of Z3Prover: https://github.com/Z3Prover/z3

--lady.py solved the Lady or the tiger problem:
KNOWLEDGE: 
There are three rooms. Each contains either a lady or a tiger but not both. Furthermore, one room contained a lady and the other two contained tigers. Each of the rooms has a sign, and at most one of the three signs was true. The three signs are:
• Room I: A TIGER IS IN THIS ROOM. • Room II: A LADY IS IN THIS ROOM. • Room III: A TIGER IS IN ROOM II.
QUESTION: 
Which room contains the lady?

--ranking.py solved the ranking problem: 
KNOWLEDGE: 
Given the following facts:
1. Lisa is not next to Bob in the ranking
2. Jim is ranked immediately ahead of a biology major
3. Bob is ranked immediately ahead of Jim
4. One of the women (Lisa and Mary) is a biology major
5. One of the women is ranked first
QUESTION: 
What are possible rankings for the four people?

