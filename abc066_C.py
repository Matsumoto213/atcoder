from collections import deque
n = int(input())
a = list(map(int, input().split()))
d = deque()
t = 0

for i in a:
    if t % 2 == 0:
        d.append(i)
    else:
        d.appendleft(i)
    t += 1

if n % 2 == 0:
    print(*d)
else:
    d.reverse()
    print(*d)