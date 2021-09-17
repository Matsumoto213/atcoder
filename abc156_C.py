n = int(input())
lst = list(map(int, input().split()))
min_lst = min(lst)
max_lst = max(lst)

result = 10 ** 8

for i in range(min_lst,max_lst + 1):
    ans = 0
    for j in lst:
        ans += abs(j - i) ** 2
    result = min(ans,result)
print(result)