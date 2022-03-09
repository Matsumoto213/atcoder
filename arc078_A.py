N = int(input())
a = list(map(int, input().split()))
temp = sum(a)

ans = 0
result = 10 ** 15
# す抜けくんがとるカードとアライグマがとるカードの総数を最小化する
for i in range(N - 1):
    temp  -= a[i]
    ans += a[i]
    result = min(result, abs(temp - ans))
print(result)

