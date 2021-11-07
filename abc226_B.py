n = int(input())
lst = []

for i in range(n):
    result = input()
    ans = result[1:]
    lst.append(ans)
print(len(set(lst)))
