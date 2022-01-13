from itertools import product
x = int(input())
INF = 1 << 60

l = [1]
temp = 1
t = 1
while temp < x:
    t += 1
    temp += t
    l.append(t)

def judge(pro):
    cnt = 0
    for i in range(t):
        if not pro[i]:
            continue
        cnt += l[i]
    
    if cnt == x:
        return t
    return INF
    
ans = INF
for pro in product((0,1), repeat = t):
    ans = min(ans, judge(pro))
print(ans)   
            


