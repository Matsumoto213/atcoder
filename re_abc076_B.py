N = int(input())
K = int(input())
start = 1

for _ in range(N):
    start = min(start * 2 , start + K)
print(start)
    