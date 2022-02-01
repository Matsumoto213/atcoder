N,S = map(int, input().split())
A = list(map(int, input().split()))


def calc(bit):
    temp = 0
    for i in range(N):
        if bit & (1 << i):
            temp += A[i]
    
    return temp


judge = False
for bit in range(1 << N):
    tem = calc(bit)
    if tem == S:
        print("Yes")
        exit(0)
        
print("No")