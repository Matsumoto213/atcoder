S = input()
from collections import Counter
C = Counter(S)

for key,value in C.items():
    if value == 1:
        print(key)
        exit()
print(-1)