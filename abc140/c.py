N = int(input())
B = list(map(int, input().split()))
A = []

for i in range(N - 2):
    A.append(min(B[i],B[i + 1]))
print(B[0] + sum(A) + B[-1])