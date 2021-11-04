n = int(input())
p = list(map(int, input().split()))

ans = 0
lst = set()

for i in p:
    lst.add(i)
    while True:
        if ans in lst:
            ans += 1
        else:
            print(ans)
            break


