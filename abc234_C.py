K = int(input())
l = [0,2,21,22,200,2,2,220,222,2000,2002,2020,2022]
i = 1
idx = 0
while True:
    if i > K:
        i //= 2
        break
    i *= 2
    idx += 1

temp = K - i

