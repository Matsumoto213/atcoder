n = int(input())
lst = []

for i in range(1,n + 1):
    ans = int(i * 1.08)
    if ans == n:
        lst.append(i)

if len(lst) == 0:
    print(":(")
else:
    print(lst[0])
