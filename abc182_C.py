from itertools import product

INF = 1 << 60

N = input()
digits = len(N)

def calc(pro):
    M = ""
    for i in range(digits):
        if pro[i]:
            M += N[i]
    
    if not M:
        return INF
    
    if int(M) % 3 == 0:
        return pro.count(0)
    else:
        return INF

ans = 100 * 8

for pro in product((0,1), repeat = N):
        ans = min(ans, calc(pro))
print(ans if ans != INF else -1)