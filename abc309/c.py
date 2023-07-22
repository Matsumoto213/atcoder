N,K = map(int, input().split())
ab = []
total = 0
for i in range(N):
    a,b = map(int, input().split())
    total += b
    ab.append((a,b))
L = sorted(ab, key=lambda x: x[0])

if total <= K:
    print(1)
    exit()

for i in range(len(L)):
    day,amount = L[i][0],L[i][1]
    total -= amount
    if total <= K:
        print(day + 1)
        exit()