def f(a, b):
    return 4 * a * b + 3 * a + 3 * b

N = int(input())
S = list(map(int, input().split()))
T = set()

for a in range(1, 1001):
    for b in range(1, 1001):
        T.add(f(a,b))
    
ans = 0

for x in S:
    if x not in T:
        ans += 1
print(ans)