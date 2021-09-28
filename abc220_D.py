# これこそ関数を使えるようになりたい
n = int(input())
a = list(map(int, input().split()))

# f f のパターン
while True:
    if len(a) == 1:
        break
    a = a[2:]
    num = (a[0] + a[1]) % 10
    lst.insert(0,num)
ans_f_f = lst[0]

# f g　のパターン
i = 0
while True:
    if len(a) == 1:
        break
    if i == 0:
        a = a[2:]
        num = (a[0] + a[1]) % 10
        lst.insert(0,num)
        i += 1
    else:
        a = a[2:]
        num = (a[0] * a[1]) % 10
        lst.insert(0,num)
    lst.insert(0,num)






    
