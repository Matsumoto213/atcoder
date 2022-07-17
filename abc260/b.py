n,x,y,z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []

a = []
b = []
total = []

for i in range(1, n + 1):
    a.append([i,A[i - 1]])
    b.append([i,B[i - 1]])
    total.append([i,A[i - 1] + B[i - 1]])

a = sorted(a, key=lambda x: x[1],reverse=True)
b = sorted(b, key=lambda x: x[1],reverse=True)
total = sorted(total, key=lambda x: x[1],reverse=True)
for i in range(x):
    ans.append(a[i][0])

cnt = 0
for i in range(n):
    if b[i][0] in ans:
        continue
    else:
        if cnt == y:
            break
        else:
            ans.append(b[i][0])
            cnt += 1
c = 0
for i in range(n):
    if total[i][0] in ans:
        continue
    else:
        if c == z:
            break
        else:
            ans.append(total[i][0])
            c += 1

ans.sort()
for i in ans:
    print(i)