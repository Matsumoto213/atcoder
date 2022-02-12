N = int(input())
ans = set()
for a in range(2,10 ** 5 + 10):
    for b in range(2,100):
        temp = a ** b
        if temp <= N:
            ans.add(temp)
        else:
            break
print(N - len(ans))
        



