n = int(input())
k = int(input())

lst = list(map(int, input().split()))

ans = 0

for i in lst:
    A = (0 + i) * 2
    B = abs((k - i) * 2)
    result = min(A,B)
    ans += result
print(ans)
