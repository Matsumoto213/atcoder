S = input()

ans = 1
s = S[0]
i = 1

while True:

    if i >= len(S):
        print(ans)
        break

    if s == S[i]:
        s = S[i: i + 2]
        i += 2
        ans += 1
        if i >= len(S):
            ans -= 1
    else:
        s = S[i]
        i += 1
        ans += 1
    