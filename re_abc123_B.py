L = [int(input()) for _ in range(5)]
l = []
num = 10 ** 8
num_idx = 0

for idx,i in enumerate(L):
    i = str(i)
    N = int(i[-1])
    if N < num and N != 0:
        num_idx = idx
        num = N

ans = 0
for index,j in enumerate(L):
    j = str(j)
    J = int(j[-1])
    if index != N or J != 0:
        n = 10 - J
        ans += int(j) + n
    else:
        ans += int(j)
print(ans)
    
    