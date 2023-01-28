N,M = map(int, input().split())
L = []
for i in range(1,10 ** 8 + 18):
    if N <= 0 and M <= 0:
        break
    # 偶数の場合
    if i % 2 == 0 and N > 0:
        N -= 1
        L.append(i)
    # 奇数の場合
    elif i % 2 != 0 and M > 0:
        M -= 1
        L.append(i)

ans = 0
for i in range(len(L) - 1):
    for j in range(i + 1,len(L)):
        if (L[i] + L[j]) % 2 == 0:
            ans += 1
print(ans)