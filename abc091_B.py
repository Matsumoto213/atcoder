import collections
n = int(input())
s = [input() for i in range(n)]

m = int(input())
t = [input() for i in range(m)]

ans = -100 ** 8

s = collections.Counter(s)
t = collections.Counter(t)
result = 0

for key,value in s.items():
    for keys,values in t.items():
        if key == keys:
            result = value - values
            break
    else:
       result = value
    ans = max(result,ans)

if ans < 0:
    print(0)
elif ans == 0:
    print(1)
else:
    print(ans)
