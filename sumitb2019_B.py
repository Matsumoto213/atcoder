import math
N = int(input())

ans = []
for i in range(N + 1):
    temp = math.floor(i * 1.08)
    if temp == N:
        ans.append(i)
        
if len(ans) == 0:
    print(":(")
else:
    print(max(ans))