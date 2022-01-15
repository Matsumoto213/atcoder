N = int(input())
L = []
for i in range(N):
    a,b = map(int, input().split())
    L.append((a,b))
    
L.sort(key = lambda x: x[1])

t = 0
judge = True
for i in range(N):
    x,y = L[i]
    
    t += x
    
    if t > y:
        judge = False
        break

print('Yes' if judge else 'No')

