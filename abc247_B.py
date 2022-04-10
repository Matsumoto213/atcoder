from re import A


N = int(input())

myoji = []
name = []

for i in range(N):
    s,t = input().split()
    myoji.append(s)
    name.append(t)

judge = True
for i in range(N):
    first = myoji[i]
    last = name[i]
    A = []
    B = []
    for j in range(N):
        if i != j:
            A.append(myoji[j])
            B.append(name[j])
    if (first in A or first in B) and (last in A or last in B):
        judge = False
print('Yes' if judge else 'No')