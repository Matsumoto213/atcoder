def zoro(n):
    L = []
    i = 1
    while True:
        k = list(str(i))
        k = set(k)
        
        if len(k) == 1:
            L.append(i)
            
        if len(L) == n:
          return L
          break
        
        i += 1
        
N = int(input())

l = zoro(N)
print(l[N - 1])