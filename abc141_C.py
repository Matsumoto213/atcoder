# 発想の転換
# 不正解した人を減らすのではなく、正解した人を増やしていく
# 重要問題
n,k,q = map(int, input().split())

lst = [k - q] * n

for j in range(q):
    a = int(input())
    lst[a - 1] += 1


for i in lst:
    if i <= 0:
        print("No")
    else:
        print("Yes")

