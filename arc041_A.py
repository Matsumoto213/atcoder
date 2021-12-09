x,y = map(int, input().split())
k = int(input())

if k < y:
  x += abs(y - k)
  print(x)
else:
  x += y
  k -= y
  if k != 0:
    x -= k
    print(x)
  
