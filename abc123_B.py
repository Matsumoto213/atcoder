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
least = 10
result = 0

for idx,i in enumerate(lst):
    i = str(i)
    hkt = int(i[-1])
    if hkt != 0:
        least = min(least,hkt)

for i,l in enumerate(lst):
    l = str(l)
    least = str(least)
    if l[-1] == least:
        result = i + 1
        break

ans = 0
for id,j in enumerate(lst):
    j = str(j)
    hitoketame = int(j[-1])
    if id != result - 1 and hitoketame != 0:
        tasu = 10 - hitoketame
        j = int(j)
        j += tasu
    ans += int(j)

print(ans)