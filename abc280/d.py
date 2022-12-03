K = int(input())

import math
ans = 1
i = 1
while True:
    i += 1
    ans *= i
    if ans % K == 0:
        print(i)
        exit()
    
    if i == 19990:
        print(K)
        exit()