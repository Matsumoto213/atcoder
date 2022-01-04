def Is(): return input()
def Iss(): return input().split()
def Ii(): return int(input())
def Iis(): return map(int,input().split())
def Iil(): return list(map(int,input().split()))
def Ixy(N): return [list(map(int, input().split())) for l in range(N)]
def Ixyind(N): 
    xy = [map(int, input().split()) for _ in range(N)]
    return [list(i) for i in zip(*xy)]
def Imixind(N):
    list = []
    for i in range(N):
        a,b=input().split()
        list.append([int(a), b])
    return list
def listtojoin(N,A):
    for i in range(N):
        a = A[i]
    print("".join(a))
def listtookuhaku(A):
    print(*A)
#####################################################################
def solve():
    from itertools import product
    ans = 0
    
    for bit in product((0,1), repeat = K):
        cnt = [0] * (N + 1) #各皿のボールをカウントする
        for i in range(K):
            # i番目の人がA_i, B_iどちらか片方にボールを置く
            # bit[i] == 0 ならA_i, bit[i] == 1ならばB_iを選びます
            ball = people[i][bit[i]]
            cnt[ball] += 1
        score = 0
        for i in range(M):
            c,d = conditions[i]
            # c,dの置いた場所が条件に当てはまっているかどうか
            if cnt[c] > 0 and cnt[d] > 0:
                score += 1
        ans = max(ans, score)
    return ans
        
N,M = map(int, input().split())

conditions = []
for _ in range(M):
    a,b = map(int,input().split())
    conditions.append((a,b))

K = int(input())
people = []
for _ in range(K):
    c,d = map(int, input().split())
    people.append((c,d))

print(solve()) 