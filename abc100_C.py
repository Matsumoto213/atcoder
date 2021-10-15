# 全て奇数になったら終了

n = int(input())
a = list(map(int, input().split()))

ans = 0
cnt = 0

for i in a:
    if i % 2 != 0:
        cnt += 1

i = 0
count = 0
while True:
    if cnt == len(a):
        break

    if i == len(a) + 1:
        cnt = 0
        count += 1
        waru = 0

    if lst[i] % 2 != 0:
        cnt += 1
        lst[i] *= 3

    elif waru == 1:
        lst[i] *= 3

    else:
        lst[i] /= 2
        waru += 1

print(count)
    
    
    

