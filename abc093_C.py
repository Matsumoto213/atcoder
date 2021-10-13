a,b,c = map(int, input().split())

lst = [a,b,c]
lst.sort()
a = lst[0]
b = lst[1]
c = lst[2]
cnt = 0

while True:
    if a == b:
        break
    if a + 2 > b:
        a += 1
        c += 1
        cnt += 1
    else:
        a += 2
        cnt += 1

cnt += c - b
print(cnt)