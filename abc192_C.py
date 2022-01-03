N,K = map(int, input().split())

def g1(n):
    n = str(n)
    n = list(n)
    n.sort(reverse = True)
    
    if n[0] == '0':
        del n[0]

    temp = "".join(n)
    temp = int(temp)
    
    return temp

def g2(n):
    n = str(n)
    n = list(n)
    n.sort()
    
    if n[0] == '0':
        del n[0]

    temp = "".join(n)
    temp = int(temp)
    
    return temp

for i in range(K):
    N = g1(N) - g2(N)
    if N == 0:
        print(0)
        exit(0)
print(N)
