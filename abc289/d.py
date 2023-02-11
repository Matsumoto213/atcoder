# 入力を受け取る
N = int(input().strip())
A = list(map(int, input().strip().split()))
M = int(input().strip())
B = list(map(int, input().strip().split()))
X = int(input().strip())

# 結果を出力する
# print("Yes" if can_climb(n, a, m, b, x) else "No")

if X in B:
    print("No")
    exit()

is_blocked = [False] * (100000 + 1)
for i in range(M):
    if B[i] <= 100000:
        is_blocked[B[i]] = True

step = [0] * (100000 + 1)
step[0] = 1
for i in range(N):
    for j in range(A[i], 100001):
        if not is_blocked[j] and step[j-A[i]] == 1:
            step[j] = 1

if step[X] == 1:
    print("Yes")
else:
    print("No")