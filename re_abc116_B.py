N = int(input())
A = []
B = set()

i = 0
while True:
    if len(A) != len(B):
        print(i)
        break
    A.append(N)
    B.add(N)
    
    if N % 2 == 0:
        N //= 2
    else:
        N = (3 * N) + 1
        
    i += 1