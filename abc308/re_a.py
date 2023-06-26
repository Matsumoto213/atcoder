N = int(input())
A = list(map(int, input().split()))

for i in range(0,N * 7,7):
    ans = sum(A[i:i + 7])
    print(ans, end = " ")
print()