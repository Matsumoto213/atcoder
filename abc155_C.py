from collections import Counter
n = int(input())
s = [input() for i in range(n)]

lst = Counter(s)
max_value = max(lst.values())

lst = sorted(lst.items())
lst = dict(lst)
for key,value in lst.items():
    if value == max_value:
        print(key)