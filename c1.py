N,Q = map(int, input().split())
A = list(map(int, input().split()))

for i in range(Q):
    n = int(input())
    A.append(n)
    A.sort()
    
    temp = A.index(n)
    print(N - temp)
    A.pop(temp)