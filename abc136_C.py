n = int(input())
h = list(map(int, input().split()))
h.reverse()
print(h)

for i in range(n - 1):
    if h[i + 1] - h[i] > 1:
        print("No")
        exit(0)
    if h[i + 1] - h[i] == 1:
        h[i + 1] = h[i]
print("Yes")