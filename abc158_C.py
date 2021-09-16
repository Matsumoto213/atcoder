a,b = map(int, input().split())
lst = []

for i in range(1,100000):
    ans1 = int(i * 0.08)
    ans2 = int(i * 0.1)
    if ans1 == a and ans2 == b:
        lst.append(i)


if len(lst) == 0:
    print(-1)
else:
    print(min(lst))