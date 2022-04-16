a,b,k = map(int, input().split())
i = 0
while True:
    if a >= b:
        print(i)
        break
    a *= k
    i += 1