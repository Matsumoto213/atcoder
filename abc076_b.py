n = int(input())
k = int(input())

for i in range(n):
    start = min(start * 2, start + k)
print(start)
