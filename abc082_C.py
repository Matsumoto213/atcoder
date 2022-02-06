from collections import Counter

N = int(input())
A = list(map(int, input().split()))

C = Counter(A)

ans = 0
# keyとvalueが揃っている中で一番大きな数を探す
for key,value in C.items():
    if key != value:
        temp = abs(key - value)
        min_ = min(temp,value)
        
        ans += min_
    
print(ans)