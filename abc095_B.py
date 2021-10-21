n,x = map(int, input().split())

m = [int(input()) for i in range(n)]
min_n = m.index(min(m))

i = 0
cnt = 0
while True:
    if x < 0:
        cnt -= 1
        break
    elif x == 0:
        break
    
    if i == len(m):
        x -= m[min_n]
        cnt += 1
    else:
        x -= m[i]
        i += 1
        cnt += 1
print(cnt)