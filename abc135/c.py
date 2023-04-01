N = int(input())
a = list(map(int, input().split()))
hp = list(map(int, input().split()))
ans = 0

for i in range(N):
    knock = min(hp[i],a[i])
    ans += knock
    hp[i] -= knock
    if hp[i] > 0:
        knock_2 = min(hp[i],a[i + 1])
        a[i + 1] -= knock_2
        ans += knock_2
print(ans)