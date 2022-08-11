N = int(input())
 
L = set()
for _ in range(N):
    n,*l = map(int, input().split())
    L.add(tuple(l))
print(len(L))