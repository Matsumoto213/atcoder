N = int(input())

def eight_divisor(n):
    divosor = 0
    for j in range(1,n + 1):
        if n % j == 0:
            divosor += 1
        
    if divosor == 8:
        return True
    
    return False

ans = 0
for i in range(1,N + 1):
    if i % 2 == 0:
        continue
    if eight_divisor(i):
        ans += 1
print(ans)