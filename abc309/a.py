a,b = map(int, input().split())
ans = [(1,2),(2,3),(4,5),(5,6),(7,8),(8,9)]

if (a,b) in ans:
    print('Yes')
else:
    print('No')