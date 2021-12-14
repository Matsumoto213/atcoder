# K = int(input())
K = 999983
N = 7

if K % 2 == 0:
    print(-1)
    exit(0)
    
while True:
    N = int(N)
    if N % K == 0:
        print(len(str(N)))
        break
    
    N = '7' + str(N)
    
