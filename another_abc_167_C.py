# bit全探索を行なって解く

INF = 1 << 60
def calc(bit):
    cnt = 0
    M = ""
    for i in range(digits):
        if bit & (1 << i):
            M += N[i]
        else:
            cnt += 1

    if not M:
        return INF
    
    if int(M) % 3 == 0:
        return cnt
    else:
        return INF

N = input()
digits = len(N)
ans = INF

for bit in range(1 << digits):
    ans = min(ans,calc(bit))

print(ans if ans != INF else -1)

