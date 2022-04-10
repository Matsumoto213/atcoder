a,b = map(int, input().split())
count = 0
i = 0

if b == 1 or b == 0:
    print(i)
    exit(0)

while True:
    if count >= b:
        break
    
    if i == 0:
        count += a
    else:
        count += a - 1
    i += 1
print(i)