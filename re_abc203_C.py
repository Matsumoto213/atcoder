N,coin = map(int, input().split())
dic = {}
A = []
for i in range(N):
    a,b = map(int, input().split())
    if a in A:
        dic[a] += b
    else:
        dic[a] = b
    A.append(a)
dic = sorted(dic.items(), key=lambda x:x[0])

now = 0
for a,b in dic:
  if now + coin <= a:
      coin -= a
      now += 
      coin += b
  else:
      print(now)