q = int(input())
ans = []
for i in range(q):
    a = list(map(int, input().split()))
    if a[0] == 0:
        ans.append(a[1])
    elif a[0] == 1:
        print(ans[a[1]])
    else:
        del ans[-1]