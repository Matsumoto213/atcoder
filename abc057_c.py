# import math

# # n = int(input())
# # num = int(math.sqrt(n))
# n = 10000

# ans = []

# for i in range(num + 1):
#     for j in range(num + 1):
#         if i * j == n:
#             ans.append([i,j])
# ans = sum(ans, [])
# result = max(ans)
# print(len(str(result)))

N = int(input())
# N = 10000
F =[]
 
 
for a in range(1, int(N ** 0.5) + 1):
  if N % a == 0:
    b = int(N / a)
    f = max(len(str(a)), len(str(b)))
    F.append(f)
    
print(min(F))