import itertools
n = int(input())
n = str(n)

all = itertools.permutations(n, len(n))
ans = []

for x in all:
    x = list(x)
    if x[0] != 0 and x[-1] != 0:
        before = "".join(x[:len(x) - 1])
        after = "".join(x[-1])
        num = int(before) * int(after)
        ans.append(num)


print(max(ans))

        
      