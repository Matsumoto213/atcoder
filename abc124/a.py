a,b = map(int, input().split())
if a == b:
    print(a * 2)
else:
    print(max(a,b) + max(a,b) - 1)