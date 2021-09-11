import math


if n == 1:
    print("Yes")

def I(): 
    return int(input())

n = I()
s = [input() for _ in range(n)]
t = [input() for _ in range(n)]

T_S = list(zip(*s))

for x in T_S[::-1]:
    print(*x,sep='')

if t == ans:
    print("Yes")
