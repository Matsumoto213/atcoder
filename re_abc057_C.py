N = int(input())
temp = int(N ** 0.5 + 1)

tem = 10 ** 11

for i in range(1, temp):
    if N % i == 0:
        s = str(int(N / i))
        i_len = len(str(i))
    lens = max(len(s),i_len)
    tem = min(lens,tem)
print(tem)