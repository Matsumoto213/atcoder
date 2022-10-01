N = int(input())
a = list(map(int, input().split()))
import bisect
cnt = 0
l = []


for i in range(N):
    idx = i
    i += 1
    if a[idx] != i:
        if i not in a:
            l.append(i)
            cnt += 1
ans = 0    
for i in range(len(l)):
    # a.insert(bisect.bisect_left(a,l[i]),l[i])
    ans += l[i]
    if l[i] not in a:
        ans -= l[i] - 1
    print(ans,a,l)
print(ans)