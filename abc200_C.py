N = int(input())
A = list(map(int, input().split()))
L = []

for i in A:
    n = i % 200
    L.append(n)
    
res = 0
for j in range(200):
    res += (b[j] * (b[k] - 1)) // 2

print(res)
    
    
    