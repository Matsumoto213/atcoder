n,k = map(int, input().split())
a = list(map(int, input().split()))

# 全員に均等にあげたのちの残数
nokori = k % n
# 全員に均等にあげる数
average = k // n

l = sorted(a)
dict = {}

for i in range(n):
    if nokori <= 0:
        dict[l[i]] = average
    else:
        dict[l[i]] = average + 1
    nokori -= 1

for i in a:
    print(dict[i])