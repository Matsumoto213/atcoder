T = int(input())

for t in range(T):
    N, K, D = map(int, input().split())

    x = K - 1
    for i in range(D):
        x = (x + D) % N
        if x == K - 1:
            break

    print(x if i == D - 1 else (K + i) % N)