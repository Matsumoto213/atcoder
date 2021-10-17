s = input()
lst = [s]


for i in range(len(s) - 1):
    s = s[-1]+s[:len(s) - 1]
    lst.append(s)
lst.sort()
print(lst[0])
print(lst[-1])