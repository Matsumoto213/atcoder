p,q = input().split()
height = {'A':0,'B':3,'C':1,'D':4,'E':1,'F':5,'G':9}
ans = 0
start = min(ord(p),ord(q))
finish = max(ord(p),ord(q))
for i in range(start + 1,finish + 1):
    ans += height[chr(i)]
print(ans)