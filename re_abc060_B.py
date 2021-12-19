A,B,C = map(int, input().split())
p = A
cnt = 0
if A % 2 == 0:
  if B % 2 == 0:
    if C % 2 != 0:
      print("NO")
      exit(0)

if A == 1:
    print("YES")
    exit(0)

while True:
    if A % B == C:
        print("YES")
        exit(0)
    else:
        A += p
    cnt += 1
    
    if cnt > 1000000:
        print("NO")
        exit(0)