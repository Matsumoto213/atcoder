h,n = map(int, input().split())
a = list(map(int, input().split()))

sum_ = sum(a)

if h - sum_ <= 0:
    print('Yes')
else:
    print('No')