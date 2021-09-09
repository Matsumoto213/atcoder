a,b,c = map(int, input().split())

lst = [a,b,c]
ans = []

for i in lst:
    ans.append(7 - i)
print(sum(ans))

