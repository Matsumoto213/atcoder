N,X = map(int, input().split())
alpha = 'ABCDEFGHIJKLMSOPQRSTUVWXYZ'

al = ""

for i in range(len(alpha)):
    al =   al + alpha[i] * N 
print(al[X - 1])
