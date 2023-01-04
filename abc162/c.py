K = int(input())

import math
ans = 0
for i in range(1,K + 1):
    for j in range(1,K + 1):
        gcd_ij = math.gcd(i,j)
        for k in range(1,K + 1):
            ans += math.gcd(gcd_ij,k)
print(ans)