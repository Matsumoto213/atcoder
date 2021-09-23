n = int(input())
lst = [int(input()) for i in range(n)]

for i in range(n):
    ans = 0
    for j in range(n):
        if i != j:
            ans = max(ans,lst[j])
    print(ans)
