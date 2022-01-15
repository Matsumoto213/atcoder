N,C,K = map(int, input().split())
t = [int(input()) for _ in range(N)]

t.sort()

# 必要なバスの数の最小値
ans = 0

i = 0
while True:
    count = 1
    if i == N:
        break
    for j in range(i + 1, i + C):
        print(i,j)
        if j > N:
            break
        temp = t[j] - t[i]
        if temp >= K:
            i = j
            ans += 1
            break
        else:
            count += 1
            if count == C:
                i += C
                ans += 1
print(ans)
        