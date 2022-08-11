N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

ans = []

for j in range(2):
    for i in range(N):
        temp = S[i - 1] + T[i - 1]
        if temp < T[i]:
            T[i] = temp

for i in range(N):
    temp = S[i - 1] + T[i - 1]
    print(min(temp, T[i]))
        