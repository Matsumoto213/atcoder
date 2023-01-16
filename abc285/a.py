a,b = map(int, input().split())
ans = a * 2
if ans == b or ans + 1 == b:
    print('Yes')
else:
    print('No')