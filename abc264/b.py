r,c = map(int, input().split())

check = max(abs(r - 8), abs(c - 8))
print('Yes' if check % 2 == 0 else 'No')