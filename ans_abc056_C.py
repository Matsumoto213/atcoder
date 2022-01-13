x = int(input())

now = 0
i = 1
ans = 0

# 超えた段階でもうそこにいくことができる
while now < x:
    now += i
    i += 1
    ans += 1
print(ans)

    