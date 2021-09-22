import itertools
n = int(input())
ans = [list(map(int,input().split(" "))) for i in range(2)]

lst = []

for i in range(1, n + 1):
    lst.append(i)

permutations = list(itertools.permutations(lst))


result = []
for i in ans:
    for idx,j in enumerate(permutations):
        j = list(j)
        if i == j:
            result.append(idx)
print(abs(result[0] - result[1]))






