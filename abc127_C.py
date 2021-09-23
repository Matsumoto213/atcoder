# 計算量を考える上で重要問題になる
# 重要問題

big,m = map(int, input().split())
lst = []
small = 1
for i in range(m):
    l,r = map(int, input().split())
    small = max(small,l)
    big = min(big,r)

if small > big:
    print(0)
else:
    print(big - small + 1)