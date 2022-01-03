N = int(input())
max_ = 0
temp = 0
ma = 0
if N == 1:
    print(1)
    exit(0)
    
for i in range(1,N + 1):
    t = 0
    idx = i
    while True:
        if idx % 2 != 0:
            break
        idx //= 2
        t += 1
    if ma < t:
        ma = t
        max_ = i
print(int(max_))