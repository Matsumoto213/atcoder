q,h,s,d = map(int, input().split())
N = int(input())

one = min(q * 4, h * 2, s)
two = min(q * 8,h * 4,s * 2,d)
ans = 0

# 最小の金額を出力する
while True:
    if N == 0:
        print(ans)
        break

    # 2より大きい時
    if N >= 2:
        ans += two
        N -= 2
    else:
        ans += one
        N -= 1