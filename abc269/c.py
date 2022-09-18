n = int(input())
ans = []
s = n
while(True):
  ans.append(s)
  if s == 0: break
  print(s - 1,bin(s - 1),n,bin(n))
  s = (s - 1) & n