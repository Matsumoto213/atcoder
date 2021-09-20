n = int(input())
lst = list(map(int, input().split()))

dic = {}
for idx, i in enumerate(lst):
    dic[i] = idx + 1

for j in range(len(lst)):
    print(dic[j + 1])