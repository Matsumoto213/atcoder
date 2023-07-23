r,d,x = map(int, input().split())
grow = x
for i in range(1,11):
    grow = ((grow * r) - d)
    print(grow)