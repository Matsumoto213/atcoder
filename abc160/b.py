x = int(input())
ans = 0
while x:
    if x >= 500 and x > 5:
        ans += 1000
        x -= 500
    elif x < 500 and x >= 5:
        ans += 5
        x -= 5
    elif x < 5:
        x = 0
print(ans)