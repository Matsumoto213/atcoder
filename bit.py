from itertools import product

def judge():
    S = 0
    for i in range(N):
        if bit & (1 << i):
            S += A[i]
    
    if S == W:
        return 1
    else:
        return 0

N, W = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
# 2進法表記で0 ～ 11...11（1がN桁）の整数をループ
# このように書いても、bitは普通の整数ですから、printすると10進法表記の3や5などになります
# なお、range(1 << N) は range(2 ** N)と同じです

for bit in range(1 << N):
    ans += judge(bit)
print(ans)