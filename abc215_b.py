n = int(input("n: "))

num = 0
ans = 0
lst = []
while True:
    ans = 2 ** num
    if ans > n:
        break
    else:
        lst.append(num)
    num += 1
print(max(lst))
