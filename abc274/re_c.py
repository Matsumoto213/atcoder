N = int(input())
A = list(map(int, input().split()))
ans = [0]*(2 * N + 1)
for i,a in enumerate(A):
    # 前の世代を一つ遡る必要があるため+1をする
    ans[2 * i + 1] = ans[a - 1] + 1
    ans[2 * i + 2] = ans[a - 1] + 1
print(*ans,sep="\n")