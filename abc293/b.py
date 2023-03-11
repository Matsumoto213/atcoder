N = int(input())
A = list(map(int, input().split()))

J = [False] * N

for i in range(N):
    if J[i] == False:
        J[A[i] - 1] = True

print(J.count(False))

for i in range(len(J)):
    if J[i] == False:
        print(i + 1, end = " ")
print()