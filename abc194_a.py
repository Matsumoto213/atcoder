# if構文の中にif構文を使っていくことに慣れていく
no_fat_milk , fat = map(int, input().split())

include_milk = no_fat_milk + fat

ans = 0

if include_milk >= 15 and fat >= 8:
    ans = 1
else:
    if include_milk >= 10 and fat >= 3:
        ans = 2
    else:
        if include_milk >= 3:
            ans = 3
        else:
            ans = 4
print(ans)