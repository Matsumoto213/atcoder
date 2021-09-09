# Greedyアルゴリズム
# Greedyアルゴリズム
# 文字を反転させる解く方法が詰め子荒れている基礎問題

s = input()
lst = ["dream","dreammer","erase","eraser"]
s = s[::-1]

# 後ろから解く代わりに全ての文字列を「左右反転」する
for i in range(4):
    lst[i] = lst[i][::-1]

can = True
for i in range(len(s)):
    can2 = False
    if i == 1:
      break
    for j in range(4):
        d = lst[j]
        if s[i:i + len(d)] == d:
            can2 = True
            i += len(d)
    if can2 == False:
        can = False
        break

if can == True:
    print("Yes")
else:
    print("No")


for i in range(10):
    if i == 2:
        i += 4
    print(i)

