# コード自体はそれほど難しくないが設計の問題や組み立て方が難しい
def judge(x, y):
    if abs(x - y) <= K:
        return True
    else:
        return False

N,K= map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[False] * 2 for _ in range(N)]
dp[0] = [True, True]

for i in range(N - 1):
    if dp[i][0]:
        if judge(A[i],A[i + 1]):
            dp[i + 1][0] = True
        if judge(A[i], B[i + 1]):
            dp[i + 1][1] = True

    if dp[i][1]:
        if judge(B[i], B[i + 1]):
            dp[i + 1][1] = True
        
        if judge(B[i], A[i + 1]):
            dp[i + 1][0] = True

if any(dp[-1]):
    print('Yes')
else:
    print('No')