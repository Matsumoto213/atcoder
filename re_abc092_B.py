N = int(input())
D,X = map(int, input().split())

for _ in range(N):
    num = 1
    interval = int(input())
    while True:
        if num > D:
            break
        num += interval
        X += 1
print(X)