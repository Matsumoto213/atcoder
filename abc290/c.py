N, K = map(int, input().split())
A = list(map(int, input().split()))

# リストAを昇順にソートする
A.sort()

ans = -10 ** 10 + 8
m = 0

# リストBを初期化する
B = A[:K]

# Bを昇順にソートし、条件を満たすmの値を求める
for i in range(K):
    if B[i] == m:
        m += 1
    else:
        break

ans = max(ans, m)
# Bの先頭の要素を除いて、リストAの次の要素を追加する
for i in range(K, N):
    B.remove(A[i-K])
    B.append(A[i])

    # Bを昇順にソートし、条件を満たすmの値を求める
    if B[0] > m:
        m = B[0]
    else:
        m = 0
        for j in range(1, K):
            if B[j] == m:
                m += 1
            else:
                break

    ans = max(ans, m)

if ans < 0:
    ans = 0

print(ans)
