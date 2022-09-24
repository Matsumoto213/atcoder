n,k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse = True)
idx = 0
cnt = 0
takahashi = 0
aoki = 0
import bisect
while n > 0:
    if cnt % 2 == 0:
        if a[idx] > n and idx != len(a) - 1:
            idx += 1
        n -= a[idx]
        if n < 0:
            n += a[idx]
            if n in a:
                takahashi += n
            else:
                temp = bisect.bisect_left(a,n)
                takahashi += a[temp]
                break
        else:
            takahashi += a[idx]
    else:
        if a[idx] > n and idx != len(a) - 1:
            idx += 1
        n -= a[idx]
        aoki += a[idx]
    cnt += 1
print(takahashi)