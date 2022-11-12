n,k,a = map(int, input().split())

cnt = 1
while True:
    if cnt == k:
        print(a)
        break
    cnt += 1
    a += 1
    if a > n:
        a = 1