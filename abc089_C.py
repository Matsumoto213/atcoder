import itertools
N = int(input())
l = ['M','R','A','C','H']
s = []


def cal(n):
    ans = 0
    for i in range(1,n + 1):
        ans += i
    return ans
        
for _ in range(N):
    S = input()[0]
    if S in l:
        s.append(S)

a = list(set(s))
p = list(itertools.combinations(s,3))

suf = len(s) - len(a)
temp = cal(suf) + 1
print(len(p),temp)

result = len(p) - temp

print(result if result > 0 else 0)



    