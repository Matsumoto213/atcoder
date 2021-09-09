n,x,t = map(int, input().split())

while True:
    if x < n:
        print(t)
        break
    t += t 
    x += x