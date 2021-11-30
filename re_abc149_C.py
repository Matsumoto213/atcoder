import math
X = int(input())

def isprime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

while True:
    if is_prime(X):
        print(X)
        break
    else:
        X += 1
        