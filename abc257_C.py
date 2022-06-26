N = int(input())
S = input()
w = list(map(int, input().split()))

mi = min(w)
ma = max(w)
ans = -10 ** 17 + 7
for i in range(max(0,mi - 100), ma + 100):
    temp = 0
    # iを設定値にする
    for j in range(len(w)):
        if i < w[j]:
            if S[j] == '1':
                temp += 1
        else:
            if S[j] == '0':
                temp += 1
    ans = max(temp,ans)
print(ans)