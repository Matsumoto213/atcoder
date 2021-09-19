X = input()
d = {x: i for i, x in enumerate(X)}
n = int(input())
S = [input() for _ in range(n)]

S.sort(key=lambda x: [*map(X.find, x)])

for s in S:
    print(s)