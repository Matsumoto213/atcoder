n = int(input())
ans = []

for i in range(1, n + 1):
    i = str(i)
    if len(i) % 2 != 0:
        ans.append(i)
print(len(ans))
