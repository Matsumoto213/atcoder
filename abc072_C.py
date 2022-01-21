N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(1)
    exit(0)

mi = min(A)
ma = max(A)
a = {}

for i in range(mi, ma + 1):
    a[i] = 0

for j in A:
    a[j] += 1
    
lenA = len(a)

max_ = -10 ** 11 + 7

idx = 0
for key,value in a.items():
    # 存在しない場合をどうするのか？
    
    if idx == 0:
        temp = value + a[key + 1]
    elif idx == lenA - 1:
        temp = value + a[key - 1]
    else:
        temp = value + a[key - 1] + a[key + 1]
    max_ = max(temp,max_)
    
    idx += 1
print(max_)
    