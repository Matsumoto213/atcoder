N = int(input())
A = list(map(int, input().split()))

for i in range(1,1000):
    for j in range(1,1000):
        ans = (4 * i * j) + (3 * i) + (3 * j)
        if ans in A:
            A.remove(ans)
print(len(A))