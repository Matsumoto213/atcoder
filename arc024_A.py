from collections import Counter
L,R = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))

l = Counter(l)
r = Counter(r)
ans = 0

for key,value in l.items():
  ans += min(r[key],value)
print(ans)