n,x = map(int, input().split())
s = input()

for i in s:
    if i == "x":
        if x == 0:
            x = 0
        else:
            x -= 1
    else:
        x += 1
print(x)
