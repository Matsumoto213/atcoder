S = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

if S == alpha[::-1]:
    print(-1)
    exit()

if S == alpha:
    print('ba')
    exit()

ans = 10 ** 18
# 文字の長さが26でなければ重複していない中で一番小さいのを最後尾に追加すればいい
if len(S) != 26:
    for i in S:
        ans = min(ord(i) - 96, ans)
    print(S + chr(ans + 97))
    