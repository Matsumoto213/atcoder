# ABC 丼： 調理時間 A 分
# ARC カレー： 調理時間 B 分
# AGC パスタ： 調理時間 C 分
# APC ラーメン： 調理時間 D 分
# ATC ハンバーグ： 調理時間 E 分

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

lst = [a,b,c,d,e]

min_least = 10
ans = 0

for i in lst:
    st = str(i)
    least = int(st[-1])
    if least > 0:
        k = 10 - least
        i += k
        min_least = min(least,min_least)
    ans += i
print(ans)