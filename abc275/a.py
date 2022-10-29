N = int(input())
H = list(map(int, input().split()))

max_value = max(H)
print(H.index(max_value) + 1)