N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
temp = 0
ans = 0
for i in range(N):
    if A[i] == B[i]:
        ans += 1
    
    if A[i] in B:
        temp += 1

print(ans)
print(temp - ans)
