a,b,c = map(int, input().split())
lst = []

for i in range(1000):
    ans = c * i
    if ans >= a and ans <= b:
        lst.append(ans)

if len(lst) == 0:
    print(-1)
else:
    print(lst[0])

