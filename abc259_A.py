N,M,X,T,D =  map(int, input().split())
if M <= N and M >= X:
    print(T)
    exit()
else:
    ans = 0
    for i in range(1,N + 1):
        if i <= X:
            ans += D
print(T - ans + (M * D))
