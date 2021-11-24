N,K = map(int, input().split())
P = []

for _ in range(N):
    p1,p2,p3 = map(int, input().split())
    ans = sum(p1,p2,p3)
    P.append(ans)

        