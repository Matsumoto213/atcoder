N = int(input())

ans = 0
btc = 380000.0

for i in range(N):
    x,u = input().split()
    x = float(x)
    if u == 'JPY':
        ans += x
    elif u == 'BTC':
        ans += x * btc
print(ans)