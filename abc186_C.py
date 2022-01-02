N = int(input())
L = set()
for ten in range(1, N + 1):
    eight = oct(ten)
    ten = str(ten)
    
    if '7' in ten:
        L.add(int(ten))
        
    if '7' in eight:
        L.add(int(eight,8))
print(N - len(L))
        
    