S = input()
N = len(S)

s_1 = S[0]
ans = 0
for idx,i in enumerate(S):
    i = int(i)
    if s_1 == "1":
        if idx % 2 == 0:
            if i == 0:
                ans += 1
        else:
            if i == 1:
                ans += 1
    else:
        if idx % 2 != 0:
            if i == 0:
                ans += 1
        else:
            if i == 1:
                ans += 1
print(ans)