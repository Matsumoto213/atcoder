N, M = map(int, input().split())
 
con = [0]*M
 
for i in range(N):
  x = list(map(int, input().split()))
  K, A = x[0], x[1:]
  for j in range(len(A)):
    con[A[j]-1] += 1
    
ans = 0
 
for i in range(M):
  if con[i] == N:
    ans += 1
    
print(ans)