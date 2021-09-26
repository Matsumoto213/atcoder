n = int(input())
lst = [input() for i in range(n)]
ans = True

if len(set(lst)) != len(lst):
    print("No")
    ans = False
else:
    for j in range(len(lst) - 1):
        if lst[j][-1] != lst[j + 1][0]:
            print("No")
            ans = False
            break

if ans:
    print("Yes")


