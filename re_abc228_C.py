N,K = map(int, input().split())
P = [sum(list(map(int, input().split()))) for i in range(N)]
L = sorted(P,reverse = True)

for i in range(N):
    P[i] += 300
    
    if P[i] >= L[K - 1]:
        print("Yes")
    else:
        print("No")
    
    P[i] -= 300