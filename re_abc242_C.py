N = int(input())

mod = 998244353
start = int('1' + '0' * (N - 1))
finish = int('1' + '0' * (N)) - 1
ans = 0

for i in range(start + 1, finish + 1):
    judge = True
    i = list(str(i))

    if '0' in i:
        continue

    