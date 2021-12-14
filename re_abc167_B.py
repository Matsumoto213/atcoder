A,B,C,K = map(int, input().split())
ans = 0

while True:
    ans += min(K,A)
    K -= min(K,A)

    if K != 0:
        K -= min(K,B)
    else:
        print(ans)
        break
    
    if K != 0:
        ans -= min(K,C)
        K -= min(K,C)
    else:
        print(ans)
        break
    
