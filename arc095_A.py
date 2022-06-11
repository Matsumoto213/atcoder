N = int(input())
X = list(map(int, input().split()))
T = sorted(X) 
mi = T[N // 2 - 1]
ma = T[N // 2]

for i in range(N):
    if X[i] == ma:
        print(mi)
    else:
        print(ma)