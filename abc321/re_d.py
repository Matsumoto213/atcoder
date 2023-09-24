import bisect
n, m, p = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

b_sum = [0] * (m + 1)
for i in range(m):
    b_sum[i + 1] = b_sum[i] + b[i]

ans = 0
print(b)
print(b_sum)
for ai in a:
    target = p - ai
    index = bisect.bisect_right(b, target)

    print(target,index)
    
    if index > 0:
        ans += b_sum[index] + ai * index
    ans += p * (m - index)
print(ans)