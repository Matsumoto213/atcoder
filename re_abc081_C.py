N = int(input())
A = list(map(int, input().split()))

cnt = 0
while True:
    even = 0
    for i in range(len(A)):
        if A[i] % 2 != 0:
            print(cnt)
            exit(0)
        else:
            even += 1
            A[i] //= 2
    if even == N:
        cnt += 1
print(cnt)         