N = int(input())
ans = set()

for i in range(N):
    S = input()
    if S not in ans and S[::-1] not in ans:
        ans.add(S)
print(len(ans))