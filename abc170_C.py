X,N = map(int, input().split())
L = set(map(int, input().split()))
for i in range(200):
    if X - i not in L:
        print(X - i)
        exit()
    
    if X + i not in L:
        print(X + i)
        exit()