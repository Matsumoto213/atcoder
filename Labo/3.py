circle = 3.1414
cnt = 1
i = 1
ans = 0
while True:
    temp = 8 / (i * (i + 2))
    ans += temp
    if circle <= ans:
        break
    cnt += 1
    i += 4
print(cnt)