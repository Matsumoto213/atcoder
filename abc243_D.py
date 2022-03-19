def solve():
    N,X = map(int, input().split())
    S = input()
    T = ["T"] # リストがからかどうかを判断するためのもの
    for s in S:
        if s == "U" and T[-1] in "LR":
            T.pop()
        else:
            T.append(s)
        print(T)

    ans = X
    for t in T[1:]:
        if t == 'U':
            ans //= 2
        elif t == "L":
            ans *= 2
        else:
            ans *= 2
            ans += 1
    return ans
print(solve())


