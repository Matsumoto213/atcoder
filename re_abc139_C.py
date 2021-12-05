# 考え方がとてもシンプルで素晴らしいコードだ
# 連続しているものを探すのであれば条件にならなかった場合に0にすればいい

N = int(input())
H = list(map(int, input().split()))
ans = - 10 ** 8
cnt = 0
for i in range(N):
    if h[i] >= h[i + 1]:
        cnt += 1
    else:
        ans = max(cnt, ans)
        cnt = 0
print(ans)