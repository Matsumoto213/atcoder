N = int(input())
a = list(map(int, input().split()))
mi = min(a)
ma = max(a)
su = mi + ma
result = 10 ** 18

if su % 2 == 0:
    temp = su // 2
    ans = 0
    for i in range(N):
        ans += (a[i] - temp) ** 2
    print(ans)
    exit()
else:
    for i in range(2):
        if i == 0:
            temp = su // 2
        else:
            temp = su // 2 + 1
        ans = 0
        for j in range(N):
            ans += (a[j] - temp) ** 2
        result = min(ans,result)
print(result)
