x = int(input())
lst = [100,101,102,103,104,105]


for i in range(len(lst)):
    if x % lst[i] == 0:
            print(1)
            exit()
    for j in range(i + 1,len(lst)):
        ans = lst[i]+lst[j]
        if x % ans == 0:
            print(1)
            exit()
print(0)



