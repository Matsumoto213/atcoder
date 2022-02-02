N = int(input())
A = list(map(int, input().split()))

def calc(bit):
    temp = 0
    for i in range(N):
        if bit & (1 << i):
            temp += A[i]
    
    return temp

ans = 0
for bit in range(1 << N):
    tem = calc(bit)
    print(tem)
    if tem == 500:
        ans += 1

print(ans)