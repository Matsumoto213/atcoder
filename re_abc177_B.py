S = input()
T = input()

ans = 10 ** 18
for i in range(len(S) - len(T) + 1):
    temp = S[i:i + len(T)]
    same = 0
    for j in range(len(T)):
        if temp[j] == T[j]:
            same += 1
    ans = min(len(T) - same,ans)
print(ans)