from itertools import product

N = int(input())
a = list(map(int, input().split()))

def judge(bit):
    ans = 0
    for i in range(N):
        if bit & (1 << i):
            print(bit)
            ans += a[i]

    return ans
        

result = 0
for bit in range(1 << N):
    temp = judge(bit)
    if temp == 1000:
        result += 1
print(result)