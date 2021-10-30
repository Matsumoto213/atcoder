n = int(input())

dic = {}

for j in range(n):
    j += 1
    dic[j] = 0


for i in range(n):
    a,b = map(int, input().split())
    dic[a] += 1
    dic[b] += 1

ans = dic.values()
result = str(n - 1)

if result in ans:
    print("Yes")
else:
    print("No")


