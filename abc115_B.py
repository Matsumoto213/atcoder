n = int(input())
lst = [int(input()) for i in range(n)]

max_num = max(lst)
print(sum(lst) - max_num + max_num // 2)