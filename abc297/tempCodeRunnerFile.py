a, b = map(int, input().split())
count = 0

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
    count += 1

print(count)
