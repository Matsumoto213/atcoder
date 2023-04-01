N,M = map(int, input().split())
import math

def find_minimum_x(N, M):
    min_product = float("inf")
    for i in range(1, int(math.sqrt(M))+1):
        print(i)
        if M % i == 0:
            if i <= N:
                j = M // i
                if j <= N:
                    min_product = min(min_product, M)
    return min_product if min_product != float("inf") else -1
result = find_minimum_x(N, M)
print(result)