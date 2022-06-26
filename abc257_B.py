n,k,q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

judge = [False] * n
for i in a:
    judge[i - 1] = True


for i in range(q):
    cnt = 0
    for j in range(n):
        if judge[j]:
            cnt += 1
            if cnt == l[i]:
                if j == n - 1:
                    continue
                else:
                    if judge[j + 1] == False:
                        judge[j] = False
                        judge[j + 1] = True


for i in range(len(judge)):
    if judge[i]:
        print(i + 1,end = " ")
print()