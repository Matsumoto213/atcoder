N,M,Q = map(int, input().split())

for i in range(Q):
    a,b,c,d = map(int, input().split())

def dfs(A):
    if len(A) == N:
        return
    for v in range(M):
        A.append(v)
        print(A,v)
        dfs(A)
        A.pop()
dfs([])