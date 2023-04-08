N,X,T = map(int, input().split())

ans = 0
quantity = 0
while True:
    if quantity >= N:
        break
    ans += T
    quantity += X
print(ans)