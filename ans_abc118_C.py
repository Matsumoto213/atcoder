import math
 
N=int(input())
A=list(map(int,input().split()))
 
ans=A[0]
for i in A:
  ans=math.gcd(ans,i)
  print(ans)
  
print(ans)