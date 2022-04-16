S = input()
N = len(S)

i = 0
ans = 0
while True:
    if i == len(S) - 1:
        print(ans)
        break
    # 連続した文字列を獲得するのであればこっちの記述の方が計算量を減らすことができる
    temp = S[i:i + 2]
    if temp == '10' or temp == '01':
        S = S[:i] + S[i + 2:]
        i -= 1
        ans += 2
    else:
        i += 1