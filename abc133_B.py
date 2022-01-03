N,D = map(int,input().split())
L = []

def is_square_num(n):
    i2 = 0
    for i in range(0, n + 1):
        if i2 == n:
            return True
        if i2 > n:
            return False
        i2 += i * 2 + 1

for i in range(N):
    l = list(map(int, input().split()))
    L.append(l)
    
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        temp = 0
        for l in range(D):
            temp += (L[i][l] - L[j][l]) ** 2
        if is_square_num(temp):
            ans += 1
print(ans)
        
    
    