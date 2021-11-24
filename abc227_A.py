n,k,a = map(int, input().split())
lst = []
cnt = 0

while True:
    if a > n:
        a = 1
    if cnt == k:
        print(lst[-1])
        break
    lst.append(a)
    a += 1    
    cnt += 1