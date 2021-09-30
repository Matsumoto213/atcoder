a,b,k = map(int,input().split())
lst = [i for i in range(a, b + 1)]

ans = lst[:k]+lst[b - a - k + 1:]

ans = list(set(ans))
ans.sort()

for i in ans:
  print(i)