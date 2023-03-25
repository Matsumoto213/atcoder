a,b,k = map(int, input().split())
L = []
for i in range(1,101):
    if a % i == 0 and b % i == 0:
        L.append(i)
print(L[-k])