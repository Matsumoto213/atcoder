n = int(input())
lst = []
 
for i in range(1, n + 1):
    num = i
    count = 0
    while True:
        if num % 2 != 0:
            lst.append(count)
            break
        else:
            num = num / 2
            count +=1
 
max_value = max(lst)
max_index = lst.index(max_value) + 1
print(max_index)
