A,B = map(int, input().split())

for i in range(1, 1001):
    a = int(i * 0.08)
    b = int(i * 0.1)
    if a == A and b == B:
        print(i)
        exit(0)
print(-1)