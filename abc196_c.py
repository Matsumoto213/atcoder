自分のコード
n = input()
num = int(n)

ans = 0

for i in range(1,num + 1):
    i = str(i)
    if len(i) % 2 == 0:
        index = int(len(i) / 2)
        right = i[:index]
        left = i[index:]
        if right == left:
            ans += 1
print(ans)



上記のコードだとだとLTEになってしまう
回答例

n = int(input())
ans = 0

for i in range(1, 1000001):
    if int(str(i) * 2) <= n:
        ans += 1
print(ans)



